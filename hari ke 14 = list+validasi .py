hasil = []
for a in range(4):
    while True:
        user = int(input("Masukkan Angka = "))
        if user <= 0:
            print("Input Tidak Boleh Nol Atau Negatif")
            continue
        hasil.append(user)
        break
print(hasil)