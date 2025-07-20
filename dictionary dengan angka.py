menu = {
    "1": "Nasi Goreng",
    "2": "Mie Ayam",
    "3": "Sate Ayam"
}
menu ["4"] = "nasi goreng"

for key, val in menu.items():
    print(f"{key} : {val}")