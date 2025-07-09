daftar_siswa = []
while True:
    nama = input("masukkan nama anda = ")
    kelas = input("kelas apa nih manieeez? =  ")
    keterangan = input("keterangan dia itu gimana ? = ")
    siswa = {
        "nama ": nama,
        "kelas ": kelas,
        "keterangan ": keterangan
    }
    daftar_siswa.append(siswa)

    ulang = input("\nApa mau ditambah lagi daftar nya (Iya/tidak)\n")
    if ulang == "tidak":
        print("\nWihhhh oke dehhh maniezzz, kaabrin ya kalau mau input lagi babayyyy !!!\n")
        break
print("\n==========DATA INPUT SISWA=========\n")
for s in daftar_siswa:
    print("Nama ==> ", s["nama "])
    print("kelas ==> ", s["kelas "])
    print("keterangan ==> ", s["keterangan "])
    print("------------------------------------")
