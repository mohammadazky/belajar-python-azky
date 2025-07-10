total_belanja= int(input("Hallo, Selamat Siang! belanja berapa hari ini? = Rp "))

if total_belanja >= 100000:
    diskon = 0.20
    pelanggan = "sangat murah hati dan tidak pelit"
elif total_belanja >50000:
    diskon = 0.10
    pelanggan = "standar murah hati dan tidak pelit"
elif total_belanja > 30000:
    diskon = 0.01
    pelanggan = "pelit"
else:
    diskon = 0

potongan = total_belanja * diskon
total_pembelian = total_belanja - potongan

print("\n================STRUCK MINI MARKET AZKI=============\n")
print("Belanja = ","Rp", total_belanja)
print("diskon = ", "Rp", int(potongan))
print("Tipe Pelanggan = ",pelanggan)
print("Harga Total Pembayaran = ", "Rp", int(total_pembelian))
print("------------=Terima Kasih Telah Berbelanja=-----------")
print("-----------=Selamat Menikmati Dan Hati2 dijalan=-----------")
