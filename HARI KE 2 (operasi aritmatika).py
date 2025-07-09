harga_roti = 5000 
harga_susu= 7000

jumlah_roti = 3
jumlah_susu = 2

total_belanja = (jumlah_roti * harga_roti) + (jumlah_susu * harga_susu)

jumlah_perorang= 3
per_orang = total_belanja / jumlah_perorang

print("Total Belanja = ", total_belanja , "Jika DIbagi Rata Perorang , maka Satu Orang(dari 3) membayar = " ,int(per_orang ))