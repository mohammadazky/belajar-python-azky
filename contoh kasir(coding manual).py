menu = {
    "1": {"nama": "Nasi Goreng", "harga": 15000},
    "2": {"nama": "Mie Ayam", "harga": 12000},
    "3": {"nama": "Es Teh", "harga": 5000}
}

total = 0
pesanan = []

# Tampilkan menu
print("=== Daftar Menu ===")
for kode, item in menu.items():
    print(f"{kode}. {item['nama']} - Rp{item['harga']}")

print("===================")

# Mulai pemesanan
while True:
    pilih = input("Masukkan kode menu (atau ketik 'selesai'): ")
    if pilih == "selesai":
        break
    if pilih in menu:
        jumlah = int(input(f"Berapa porsi {menu[pilih]['nama']}? "))
        harga_pesanan = menu[pilih]['harga'] * jumlah
        total += harga_pesanan
        pesanan.append((menu[pilih]['nama'], jumlah, harga_pesanan))
    else:
        print("Menu tidak ditemukan!")

# Cetak struk
print("\n=== Struk Pembelian ===")
for nama, jumlah, subtotal in pesanan:
    print(f"{nama} x{jumlah} = Rp{subtotal}")
print(f"Total Bayar: Rp{total}")
print("=======================")
