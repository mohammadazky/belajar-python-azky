angka = []
for a in range(5):
    while True:
        pengguna = int(input("Masukkan Angka = "))
        if pengguna == 0:
            print("Dilarangnol!!")
            continue
        angka.append(pengguna)
        break
print(angka)
