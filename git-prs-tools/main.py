import logging
from git_tools.git_operations import generate_git_commands

# Setup logging untuk mencatat semua perintah yang dijalankan
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Masukkan informasi yang dibutuhkan dari pengguna
    branch_name = input("Masukkan nama branch: ")
    commit_message = input("Masukkan pesan commit: ")
    tag_name = input("Masukkan nama tag: ")
    tag_commit_message = input("Masukkan pesan commit untuk tag: ")

    # Menjalankan fungsi untuk membuat perintah git dan PR
    generate_git_commands(branch_name, commit_message, tag_name, tag_commit_message)

if __name__ == "__main__":
    main()
