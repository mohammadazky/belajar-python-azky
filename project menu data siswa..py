data_siswa = []

def nambah_siswa():
    while True:
        print("\n===========*TAMBAH DATA SISWA*=================\n")
        user = input("Silahkan Masukkan Nama Yang Mau Diinpput = ")
        classs= input(f"Kelasnya atas nama siswa {user} Itu Kelas Apa = ")
        skill = input(f"Jurusan Apa {user} Ini = ")
        data_siswa.append({
            "nama" : user,
            "kelas" : classs,
            "Jurusan" : skill
        })
        print(f"Data Atas Nama {user} Berhasil Ditambahkan!")
        tanya = input("\nApa Mau Nambah Lagi Datanya ? [iya/tidak] = \n")
        if tanya != "iya":
            break


  

def tampilkan():
    if len(data_siswa) == 0:
        print("Tidak Ada Data Siswa Yang Ditambahkan!!")
    else:
        for a, siswa in enumerate(data_siswa, start=1):
            print(f"{a} Nama = {siswa['nama']}")
            print(f"    kelas = {siswa['kelas']}")
            print(f"    Jurusan = {siswa['Jurusan']}")

def siswa_dicari():
    nama = input("Atas Nama Siapa Nama Yang Mau Dilihatnya ? = ")
    ketemu = False
    for siswa in data_siswa:
        if siswa['nama'].lower() == nama.lower:
            print(f"{siswa} {siswa['nama']} {siswa['kelas']} {siswa['Jurusan']}")
            ketemu = True
            break
    if not ketemu:
        print(f"Siswa Dengan Nama : {nama} status data =  Tidak Ada!!")

def menu():
    print(f"\n=================*DATA SISWA SMAN 1 ALKAMIL*===============\n")
    print("Pilihan Menu = ")
    print("1. Menambah Data Siswa")
    print("2. Mencari Profil Siswa SMAN 1 ALKAMIL")
    print("3. Melihat Data Siswa ")
    print("4. Keluar Dari Menu")
    while True:
        try:
            pilih = int(input("\nMau Pilih Menu Nomer Berapa ? ="))
            if pilih == 1:
                nambah_siswa()
            elif pilih == 2:
                siswa_dicari()
            elif pilih == 3:
                tampilkan()
            else:
                break
        except ValueError:
            print("Masukkan Pilihan Dengan Angka Ya Maniss")

menu()






