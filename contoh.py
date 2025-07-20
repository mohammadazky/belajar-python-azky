print("=== Selamat Datang di Kasir Azki ===\n")
daftar_belanja = []
total_harga = 0

while True:
    nama_barang = input("Nama Barang : ")
    while True:
        try:
            harga_barang = int(input("Harga Barang : Rp "))
            break
        except ValueError:
            print("Masukkan harga dalam angka ya, maniess!")

    daftar_belanja.append({"barang": nama_barang, "harga": harga_barang})
    total_harga += harga_barang

    lanjut = input("Mau tambah barang lagi? (ya/tidak): ").lower()
    if lanjut != "ya":
        break

# Tampilkan Daftar Belanja di Terminal
print("\n=== STRUK BELANJA AZKI ===\n")
for index, item in enumerate(daftar_belanja, start=1):
    print(f"{index}. {item['barang']} - Rp {item['harga']}")

print(f"\nTotal Belanja : Rp {total_harga}")

# Simpan Struk ke File Txt
with open("Struk-Belanja-Azki.txt", "w") as file:
    file.write("=== STRUK BELANJA AZKI ===\n\n")
    for index, item in enumerate(daftar_belanja, start=1):
        file.write(f"{index}. {item['barang']} - Rp {item['harga']}\n")
    file.write(f"\nTotal Belanja : Rp {total_harga}\n")

print("\nStruk Belanja Tersimpan di File Txt. Terima kasih!")
