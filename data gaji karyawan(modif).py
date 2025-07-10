nama_karyawan = input("\nHalloo, Ini dengan karyawan PT AZKY TECH namanya siapa ya ? nama = \n")
try:
    gaji_pokok = int(input(f"hallo Mas/Mbak {nama_karyawan} Gaji kamu berapa nih = "))
except ValueError:
    print("Masukiin gajinya dengan angka ya mbak/mas , masa gak tau kayak Anak TK aja!")
jam_kerja = int(input("Berapa Jam Kerja Anda Sehari ? = "))
if gaji_pokok >= 15000000:
    persen_gaji = 15
elif gaji_pokok <= 1000000:
    persen_gaji = 10
else:
    persen_gaji = 5
if jam_kerja >=8:
    jam_lembur = jam_kerja - 8
    bonus_lembur = jam_lembur *30000 
else:
    jam_lembur = 0
    bonus_lembur = 0

gaji_total = gaji_pokok + bonus_lembur
pajak = gaji_total * persen_gaji // 100
gaji_bersih = gaji_total - pajak

print("\n============DATA GAJI KARYAWAN=========\n")
print(f"\nNama = {nama_karyawan}\n")
print(f"\nGaji Pokok = {gaji_pokok}\n")
print(f"\nBonus Lembur = {bonus_lembur}\n")
print(f"\nPajak Gaji = ({persen_gaji}%) : Rp {pajak} \n")
print(f"\nGaji bersih {nama_karyawan} adalah = Rp{gaji_bersih} IDR")



