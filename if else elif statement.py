try:
    umur = int(input("Masukkan umur anda ="))
except ValueError:
    print("Harus angka ya manieeezzz, masukiin nya!!!")
    exit()
if umur <5:
    print("Kategori = bayi")
elif umur >= 5 and umur <= 12:
    print("Kategori = Anak Anak")
elif umur >= 13 and umur <= 17:
    print("Kategori = remaja")
elif umur >= 18 and umur <=59:
    print("Kategori = dewasa")
else:
    print("Kategori = lansia")
