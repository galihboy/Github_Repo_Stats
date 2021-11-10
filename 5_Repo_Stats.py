'''
    Monitoring statistik data harian dari repository Github
    By Galih Hermawan
    https://galih.eu
    https://galihboy.github.io
'''
from github import Github
from operator import itemgetter

lstTipe = [0,0] # menyimpan jml repo tipe private/public

# Buat instance Github + akses token personal
g = Github("token") # isi token akses di sini

# akses repository
aksesRepo = g.get_user().get_repos()

# menelusuri semua repo
for no, repo in enumerate(aksesRepo):
    # cek tipe repo
    if repo.private: 
        tipe = "Private" 
        lstTipe[0] += 1
    else:
        tipe = "Public"
        lstTipe[1] += 1

    # Info repository
    print(f"Repository ke-{no + 1}: {repo.name}")
    print(f"  Tipe: {tipe}") #public/private
    jmlBintang = repo.stargazers_count
    print(f"  Jumlah bintang: {jmlBintang}")

    # data clone harian
    data_clone = repo.get_clones_traffic(per="day")
    print("\nData Clone.")
    print(f"  Jumlah clone total: {data_clone['count']}")
    print(f"  Jumlah clone unik: {data_clone['uniques']}")
    if data_clone:
        for i, data in enumerate(data_clone['clones']):
            print(f"  · Clone ke-{i + 1} = tanggal: {data.timestamp}, total: {data.count}, jumlah unik: {data.uniques}")

        # menghitung dan mencari data clone terbanyak
        if len(data_clone['clones']) > 1:
            data_clone_terbanyak = max(*list((day.count, day.timestamp) for day in data_clone["clones"]), key=itemgetter(0))
            print(f"  Clone paling banyak pada {data_clone_terbanyak[1]} dengan total {data_clone_terbanyak[0]} salinan.")
    else:
        print("  Tidak ada data clone.")

    # data view harian
    data_view = repo.get_views_traffic(per="day")
    print("\nData View.")
    print(f"  Jumlah view total: {data_view['count']}")
    print(f"  Jumlah view unik: {data_view['uniques']}")
    if data_view:
        for i, data in enumerate(data_view['views']):
            print(f"  · View ke-{i + 1} = tanggal: {data.timestamp}, total: {data.count}, jumlah unik: {data.uniques}")

        # menghitung dan mencari data view terbanyak
        if len(data_view['views']) > 1:
            data_view_terbanyak = max(*list((day.count, day.timestamp) for day in data_view["views"]), key=itemgetter(0))
            print(f"  View paling banyak pada {data_view_terbanyak[1]} dengan total {data_view_terbanyak[0]} tampilan.")
    else:
        print("  Tidak ada data view.")

    # konten populer
    data_populer = repo.get_top_paths()
    print("\nData populer.")
    if data_populer:
        for i, data in enumerate(data_populer):
            print(f"  Data ke-{i+1}.")
            print(f"  · Judul: {data.title}")
            print(f"  · Path: {data.path}")
            print(f"  · Jumlah akses: {data.count}")
            print(f"  · Jumlah akses unik: {data.uniques}")

        # menghitung dan mencari data path populer terbanyak
        if len(data_populer) > 1:
            populer = max(*list((day.count, day.path) for day in data_populer), key=itemgetter(0))
            print(f"  Data path terpopuler adalah '{populer[1]}' - sudah dilihat {populer[0]} kali.")
    else:
        print("  Tidak ada data populer.")

    # Top referrer (perujuk) dalam 14 hari terakhir
    data_referrer = repo.get_top_referrers()
    print("\nData Referrer (Perujuk).")
    if data_referrer:
        for i, data in enumerate(data_referrer):
            print(f"· Referrer ke-{i+1}: {data.referrer}, jumlah: {data.count}, unik: {data.uniques}")
    else:
        print("· tidak ditemukan data referrer.")
    print("\n--------------------------------------\n")

print(f"Jumlah repository tipe Private: {lstTipe[0]}, Public: {lstTipe[1]}, total: {aksesRepo.totalCount}")

