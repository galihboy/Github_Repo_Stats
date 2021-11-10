from github import Github

# Buat instance Github + akses token personal
g = Github("token") # isi token akses di sini

# inisialisasi jml repo berdasarkan tipe (private atau public)
jmlRepoPrivate = 0
jmlRepoPublic = 0

# akses repository
aksesRepo = g.get_user().get_repos()

# menelusuri semua repo
for no, repo in enumerate(aksesRepo):
    if repo.private:
        jmlRepoPrivate += 1
        tipe = "Private"
    else:
        jmlRepoPublic += 1
        tipe = "Public"

    print(f"Repository ke-{no+1}: {repo.name}, tipe: {tipe}")

print(f"\nJumlah repository tipe Private: {jmlRepoPrivate}, Public: {jmlRepoPublic}, total: {aksesRepo.totalCount}")
