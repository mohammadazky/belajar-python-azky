ussername_benar = "MOHAMMADAZKY12"
password_benar = "Tasikmalaya12"
pin_benar = 20070817
kode_rahasia = 170807

print("\n============MENU ACCOUNT=============\n")
print("1. login account bank")
print("2. cek data account\n")

pilihan = input("Masukkan pilihan anda dari menu manieez ===> (1/2) = ")

if pilihan == "1":
    percobaan = 3
    while percobaan > 0:
        us = input("Masukkan username anda = ")
        if us == ussername_benar:
            pw = input("Masukkan password anda = ")
            if pw == password_benar:
                while percobaan > 0:
                    pin = int(input("Masukkan PIN account bank anda ===> = "))
                    if pin == pin_benar:
                        print("✅ DATA LOGIN BENAR !!, SILAHKAN MASUK MANIEEEZ !")
                        percobaan = 0
                        break
                    else:
                        percobaan -= 1
                        if percobaan > 0:
                            print("⚠️ PIN ANDA SALAH !!, SISA PERCOBAAN ===>", percobaan)
                        else:
                            print("⚠️ PIN SALAH!!, TIDAK ADA PERCOBAAN TERSISA")
                break
            else:
                print("❌ CAKRA! PASSWORD ANDA SALAH!")
                break
        else:
            print("❌ CAKRA! USERNAME ANDA SALAH! AKSES DITOLAK!")
            break

elif pilihan == "2":
    percobaan = 3
    while percobaan > 0:
        kode = int(input("Masukkan kode rahasia, untuk membuka akses data ===> = "))
        if kode == kode_rahasia:
            print("\n✅ ======= ACCOUNT ANDA =======\n")
            print("USERNAME =", ussername_benar)
            print("PASSWORD =", password_benar)
            print("PIN ANDA =", pin_benar)
            break
        else:
            percobaan -= 1
            if percobaan > 0:
                print("⚠️ Kode rahasia salah!!, SISA PERCOBAAN ===>", percobaan)
            else:
                print("⚠️ Kode rahasia salah! Tidak ada percobaan tersisa")
else:
    print("❌ CAKRA! Pilihan tidak valid!!!")


        
        

