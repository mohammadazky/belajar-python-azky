angka = int(input("masukkan angka anda ="))
if angka  %2 == 0 and angka >50:
    print("ANGKA GENAP DAN LEBIH BESAR DARI 50")
elif angka %2 != 0 and angka <50:
    print("Angka ganjil dan kurang dari 50")

else:
    print("kriteria tidak memenuhi")