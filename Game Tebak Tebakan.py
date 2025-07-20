import random
nama_games = "GAMES MENEBAK KUCING"
kucing= random.randint(1,5)




nama_pemain = input("Siapa Nama Anda = ")
print(f"========{nama_games}============")
print(f"Hallo Selamat Datang {nama_pemain} \n Semoga Seru Ya Gamenya\n")
print("\nsilahkan ikuti instruksi ya\n")
print("\n*******ketentuan Bermain*********\n")
print("-Jawab Dengan Mengetik Angka ya")
print("Jika Salah, Ada Kesempatan 3 kali")
print("Have Fun Maniesss, terima kasih")

print("==========GAMENYA========== ")

print("Kucing Ada Dijerami Mana(1/2/3/4/5) = ")



percobaan = 3 
while percobaan>0:
    try:
        user= int(input("Masukkan Jawaban Anda (1/2/3/4/5)="))
        if user <1 or user >5:
            print("Jawaban Kamu Melebihi jawaban yang diinginkan (cukup 1 angka saja)")
            continue
        keyakinan = input("Apakah Kamu Yakin Dengan Tebakan Kamu (y/t)=").lower()
        if keyakinan == "y":
            if user == kucing :
                print("Hore Tebakanmu Benar !!!! Kucing Ada Dijerami ",kucing , "Jawabanmu = ", user)
                break
            else:
                percobaan -= 1
                if percobaan >0:
                    print("Jawabanmu Salah!!! ada sisa kesempatan = ", percobaan)
                else:
                    print("Jawabanmu sudah salah!!! coba lagi lain waktu ya")
        elif keyakinan == "t":
            print("Kamu Pikirkan Dengan Baik Ya untuk menjawabnya manieess")
        else:
            print("Input y atau tidak!!")
    except ValueError:
        print("Masukkan Angka jawaban Selain Itu Salah!! dan Game bisa berhenti!!")





