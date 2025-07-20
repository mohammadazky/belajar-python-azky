print("\n====**WELCOME TO KASIR MALL AZKI MART**====\n")
daftar_belanja = []
total_harga = 0

while True:
    nama_barang = input("Masukkan Nama Barang Belanjaan Anda = ")
    while True:
        try:
            harga_barang = int(input(f"Berapa Harga Yang Tertera Di ==> {nama_barang} ="))
            break
        except ValueError:
            print("Masukkan Harga Barang Itu Ya Angka IDR oon!!")

    daftar_belanja.append({"Nama Barang" : nama_barang, "Harga Barang" : harga_barang})
    total_harga  += harga_barang

    tambah = input("Apa Masih Ada Barang Lain Yang Dibeli ?(ada/tidak) = ").lower()
    if tambah != "ada":
        break
    
print("\n====STRUK AZKI MART====\n")
for index, item in enumerate(daftar_belanja, start=1):
    print(f"{index}. {item['Nama Barang']} - Rp {item['Harga Barang']}")

print(f"\nTotal Belanja = Rp {total_harga}")

with open("Struk-AZKI-mart.txt.","w") as file:
    file.write("\n======STRUK BELANJA AZKI MART=========\n")
    for index, item in enumerate(daftar_belanja, start=1):
        file.write(f"{index} . {item['Nama Barang']}  -Rp{item['Harga Barang']}\n")
    file.write(f"\nTotal Belanja Anda = {total_harga}\n")

print("Data Belanjaan Anda Tersimpan Ke STRUK AZKI MART.txt TERIMAKASIH!! ")
print("Jangan Lupa Belanja Lagi Manieeezz")






