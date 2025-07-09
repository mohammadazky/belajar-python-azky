nama = input("Siapa nama anda =")
try:
    gaji = int(input("Berapa gaji anda = "))
except ValueError:
    print("Awas!! gaji harus angka ya ")
    exit()

if gaji >= 5000001 and gaji <= 9999999: 
    persen_gaji = 8
elif gaji >= 10000001 and gaji <= 14999999:
    persen_gaji = 12
elif gaji < 5000000:
    persen_gaji = 0
else:
    persen_gaji = 20


pajak = gaji * persen_gaji // 100
gaji_bersih = gaji - pajak


print("\n================DATA GAJI KARYAWAN=============\n")
print(f"\n Nama karyawan = {nama}\n")
print(f"\n gaji kotor  = {gaji} \n")
print(f"\n Pajak = ({persen_gaji}%) : Rp {pajak} \n")
print(f" Gaji bersih = Rp {gaji_bersih}")

