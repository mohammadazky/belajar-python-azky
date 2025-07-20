menu = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Es Teh": 5000
}

pesanan = ["Nasi Goreng", "Es Teh"]

jumlah = 0
for item in pesanan:
    jumlah += menu[item]

print("Total = {jumlah}")
    