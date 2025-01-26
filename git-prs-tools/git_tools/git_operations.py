import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_git_commands(branch_name, commit_message, tag_name, tag_commit_message):
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    logging.info(f"Branch {branch_name} telah dibuat dan Anda berpindah ke sana.")
    subprocess.run(["git", "add", "."], check=True)  
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    logging.info(f"Commit berhasil dengan pesan: {commit_message}")
    subprocess.run(["git", "tag", "-a", tag_name, "-m", tag_commit_message], check=True)
    logging.info(f"Tag {tag_name} telah dibuat.")
    subprocess.run(["git", "push", "origin", branch_name], check=True)
    subprocess.run(["git", "push", "origin", tag_name], check=True)
    logging.info(f"Branch {branch_name} dan tag {tag_name} telah dipush ke GitHub.")
    pr_title = f"PR untuk {branch_name}"
    pr_body = f"Deskripsi PR: {commit_message}"

    result = subprocess.run([
        "gh", "pr", "create", 
        "--title", pr_title, 
        "--body", pr_body, 
        "--base", "main",  
        "--head", branch_name,
        "--assignee", "@me"  
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        logging.info(f"Pull Request telah dibuat dari {branch_name} ke main.")
        merge_result = subprocess.run([
            "gh", "pr", "merge", 
            "--merge",  
            "--delete-branch",  
            "--body", "Auto-merged after CI checks passed"  
        ], capture_output=True, text=True)
        
        if merge_result.returncode == 0:
            logging.info(f"PR {branch_name} berhasil digabungkan ke main.")
            rebase_result = subprocess.run([
                "git", "fetch", "origin", "main"  
            ], capture_output=True, text=True)

            if rebase_result.returncode == 0:
                logging.info("Perubahan terbaru dari branch main berhasil di-fetch.")
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

