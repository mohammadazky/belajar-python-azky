data_siswa = []
count = 0

while True:
    print("\n===********DATA SISWA PROJECT********======\n")
    nama = input("Nama Lengkap = ")
    while True:
        try:
            umur = int(input("Umur = "))
            if umur <16 or umur >18:
                print("Masukkan Umur Yang Masuk Kategori Usia Anak Sma Maniess!!")
                continue
            break
        except ValueError:
            print("Hei OON!! Umur Diinput Hanya Bentuk Angka!!!")
            print("Manis 2x Ko bodoh!!")


    alamat = input("Alamat Lengkap = ")
    jurusan = input("Jurusan = ")

    siswa = {
        "nama": nama,
        "umur": umur,
        "alamat": alamat,
        "jurusan": jurusan

    }
    data_siswa.append(siswa)
    count += 1

    if count %5 == 0:
        tanya = input("Apakah Mau Lanjut Ngisi Data Manies?  (iya/tidak) = ")
        if tanya.lower() == "tidak":
            break
print("\n==========*Data Siswa*===========\n")
for index, siswa in enumerate(data_siswa, start=1):
    print(f"\nSiswa ke = {index}: ")
    for key, val in siswa.items():
        print(f"{key} : {val}")

with open("Data-siswa-project-azky.txt", "w") as file:
    for index, siswa in enumerate(data_siswa, start=1):
        file.write(f"Siswa Ke - {index}:\n")
        for key, val in siswa.items():
            file.write(f"{key} : {val}\n")
        file.write("\n")
print("Data Anda Tersimpan Ke File 'Data-siswa-project-azky.txt'.")
        


