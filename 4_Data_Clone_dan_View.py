from github import Github
'''
    Menampilkan data clone dan view dari repository Github
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
    # data clone
    data_clone = repo.get_clones_traffic(per="week")
    print("Data Clone.")
    print(f"  Jumlah clone total: {data_clone['count']}")
    print(f"  Jumlah clone unik: {data_clone['uniques']}")
    if data_clone:
        for i, data in enumerate(data_clone['clones']):
            print(f"    Clone ke-{i+1} = tanggal: {data.timestamp}, total: {data.count}, jumlah unik: {data.uniques}")
    # data view
    data_view = repo.get_views_traffic(per="week")
    print("Data View.")
    print(f"  Jumlah view total: {data_view['count']}")
    print(f"  Jumlah view unik: {data_view['uniques']}")
    if data_view:
        for i, data in enumerate(data_view['views']):
            print(f"    View ke-{i + 1} = tanggal: {data.timestamp}, total: {data.count}, jumlah unik: {data.uniques}")

