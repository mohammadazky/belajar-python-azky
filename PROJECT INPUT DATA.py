count = 0
data_karyawan= []

while True:
    print("\n======**DATA KARYAWAN AZKI**======\n")
    nama = input("Nama = ")
    while True:
        try:
            umur = int(input("Umur = "))
            if umur <18:
                print("Umur Kamu Dibawah Umur Tidak Bisa Jadi karyawan ")
                continue
            
            elif umur >50:
                print("Usia Kamu Tua Banget , Maksimal 49 tahun ya!!")
                continue
            break
        except ValueError:
            print("Masukkan Data Umur Pakai Angka Ya Maniess")    

    ttl = input("Tempat/tanggal lahir = ")
    alamat = input("Alamat = ")
    while True:
        status = input("Status = ")
        if status in ("Single","sudah menikah"):
            break
        else:
            print("Masukkan Status Single / Sudah Menikah ")
    
    data= {
        "nama": nama,
        "umur": umur,
        "ttl" : ttl,
        "alamat": alamat,
        "status": status

    }
    data_karyawan.append(data)
    count += 1
    if count %3 == 0:
        tanya = input("Apakah Mau Lanjut Ngisi Data Karyawannya Maniess (iya/tidak)= ").lower()
        if tanya != "iya":
            break
print("\n=====**DATA KARYAWAN AZKI**=====\n")
for index, karyawan in enumerate(data_karyawan,start=1):
    print(f"karyawan ke - {index} ")
    for key, val in karyawan.items():
        print(f"{key} : {val}")

with open("Data-Karyawan-Azky.txt", "w") as file:
    for index, karyawan in enumerate(data_karyawan, start=1 ):
        file.write(f"Karyawan ke - {index}\n")
        for key, val in karyawan.items():
            file.write(f"{key.capitalize():<8} : {val}\n")
        file.write("\n")
print("Data Yang Anda Masukkan Tersimpan Ke File Txt")


    


    