nama = input("masukkan nama anda =  ")
umur = int(input("masukkan umur anda = "))
tinggi = float(input("masukkan tinggi anda ="))
hitung_umur = umur * 2
integer_tinggi = int(tinggi)
if umur >18:
    status = "sudah dewasa"
else:
    status = "belum dewasa"
print(f"halo {nama}  umur kamu  {umur} dua kali umur kamu {hitung_umur} tinggi kamu {integer_tinggi}, apakah dewasa? {status}")
