data_siswa = {
    "nama": "Azki",
    "umur": 17,
    "kelas": "XII Multimedia"
}
data_siswa ["status"] = "aktif"
print("\nNama Azky = ", data_siswa["nama"], "\numur azky = ", data_siswa["umur"],"\nkelas azki = ",data_siswa["kelas"], "\nstatus azki = ",data_siswa["status"] )
for key, val in data_siswa.items():
    print(f"data {key} adalah {val}")