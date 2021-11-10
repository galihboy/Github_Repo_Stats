from github import Github
'''
    Menampilkan data clone (mentah) dari repository Github
    By Galih Hermawan
    https://galih.eu
    https://galihboy.github.io
'''

# Buat instance Github + akses token personal
g = Github("token") # isi token akses di sini

# akses repository
aksesRepo = g.get_user().get_repos()
print(f"Jumlah repository: {aksesRepo.totalCount}")

# menelusuri semua repo
for no, repo in enumerate(aksesRepo):
    print(f"\nRepository ke-{no + 1}: {repo.name}")
    data_clone = repo.get_clones_traffic(per="week")
    print(data_clone)

