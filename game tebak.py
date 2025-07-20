import random
pesan_game= "WELCOME TO TEBAK TEBAKAN ORANG DI SUNGAI"
sungai_posisi = random.randint(1,3)

print(f"********{pesan_game}*************")
print("SiAPKAN JAWABANMUU!!")

nama_pemain= input("Siapa Nama Anda = ")
print(f"Hallo {nama_pemain} Semoga Seru Ya!! Gamenya!!")
print("Gamenya Dimulai Sekarang!!!")
print("Ada Dimanakah Orang Berada Disungai (1/2/3) = ")

percobaan = 3
while percobaan > 0:
    try:
        user = int(input("Masukkan Tebakan Kamu = "))
        if user <1 or user >3:
            print("Harus Angka 1 sampai 3 yaa!!! manieess")
            continue
        keyakinan= input("Apakah Kamu Yakin Dengan Jawabanmu ? (y/tidak) = ").lower()
        if keyakinan == "y":
            if user == sungai_posisi:
                print(f"Horeee Tebakan Kamu Berhasil Orang Ada Di sungai Ke {sungai_posisi} dan pilihanmu {user}")
                break
            else:
                percobaan-=1
                if percobaan >0:
                    print(f"Salahhhhh!!!kamu kalah!! Sisa Percobaan = {percobaan}")        
                else:
                    print("Kamu Kalah!! orangnya ada di = ",sungai_posisi)

        elif keyakinan == "tidak":
            print("Oke Kamu Bisa Ganti Jawabanmu")
        else:
            print("Jawab Y untuk Yakin dan tidak untuk Belum yakin ya")
    except ValueError:
        print("Tidak Valid !! masukkan tebakkan berupa angka ya Maniezz")
