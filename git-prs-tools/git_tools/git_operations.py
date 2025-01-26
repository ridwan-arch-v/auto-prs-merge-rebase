import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_git_commands(branch_name, commit_message, tag_name, tag_commit_message):
    """
    Fungsi ini akan menjalankan perintah git untuk membuat branch, melakukan commit, 
    membuat tag, dan push ke GitHub, lalu membuat Pull Request, menggabungkannya,
    dan melakukan rebase pada main.
    """
    # Checkout ke branch baru
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    logging.info(f"Branch {branch_name} telah dibuat dan Anda berpindah ke sana.")
    
    # Menambahkan perubahan (termasuk untracked files) dan commit
    subprocess.run(["git", "add", "."], check=True)  # Menambahkan semua file yang ada (termasuk untracked)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    logging.info(f"Commit berhasil dengan pesan: {commit_message}")
    
    # Membuat tag
    subprocess.run(["git", "tag", "-a", tag_name, "-m", tag_commit_message], check=True)
    logging.info(f"Tag {tag_name} telah dibuat.")
    
    # Push ke GitHub
    subprocess.run(["git", "push", "origin", branch_name], check=True)
    subprocess.run(["git", "push", "origin", tag_name], check=True)
    logging.info(f"Branch {branch_name} dan tag {tag_name} telah dipush ke GitHub.")
    
    # Membuat Pull Request menggunakan GitHub CLI
    pr_title = f"PR untuk {branch_name}"
    pr_body = f"Deskripsi PR: {commit_message}"

    # Membuat Pull Request
    result = subprocess.run([
        "gh", "pr", "create", 
        "--title", pr_title, 
        "--body", pr_body, 
        "--base", "main",  # Ganti dengan branch tujuan (misalnya "main")
        "--head", branch_name,
        "--assignee", "@me"  # Opsional: Bisa menambahkan assignee jika perlu
    ], capture_output=True, text=True)
    
    # Cek apakah PR berhasil dibuat
    if result.returncode == 0:
        logging.info(f"Pull Request telah dibuat dari {branch_name} ke main.")
        
        # Auto-merge PR jika berhasil dibuat
        # Hanya satu opsi yang boleh digunakan --merge atau --rebase atau --squash
        merge_result = subprocess.run([
            "gh", "pr", "merge", 
            "--merge",  # Gunakan opsi --merge untuk merge biasa
            "--delete-branch",  # Menghapus branch setelah merge
            "--body", "Auto-merged after CI checks passed"  # Optional body text
        ], capture_output=True, text=True)
        
        # Cek hasil merge
        if merge_result.returncode == 0:
            logging.info(f"PR {branch_name} berhasil digabungkan ke main.")
            
            # Lakukan auto-rebase pada branch main setelah merge
            rebase_result = subprocess.run([
                "git", "fetch", "origin", "main"  # Mengambil perubahan terbaru dari branch main
            ], capture_output=True, text=True)

            if rebase_result.returncode == 0:
                logging.info("Perubahan terbaru dari branch main berhasil di-fetch.")
                
                # Lakukan rebase untuk memastikan branch main sudah update
                rebase_result = subprocess.run([
                    "git", "rebase", "origin/main"
                ], capture_output=True, text=True)

                if rebase_result.returncode == 0:
                    logging.info("Branch main berhasil di-rebase dengan perubahan terbaru dari GitHub.")
                else:
                    logging.error(f"Gagal melakukan rebase: {rebase_result.stderr}")
            else:
                logging.error(f"Gagal melakukan fetch dari main: {rebase_result.stderr}")
        else:
            logging.error(f"Gagal menggabungkan PR {branch_name} ke main. Error: {merge_result.stderr}")
    else:
        logging.error(f"Gagal membuat Pull Request: {result.stderr}")

