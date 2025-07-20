data_siswa = {
    "nama" : "mohammad azky",
    "umur": 17,
    "kelas" : "xii",
    "jurusan" : "multimedia"
    
}

print("umur azki = ", data_siswa["umur"])
data_siswa ["status"] = "aktif" # menambah key dan value
for key, val in data_siswa.items():
    print(f"{key} : {val}")
