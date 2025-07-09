ussername_benar = "mohammad azky "
password_benar = "azkikamill0"
pin_benar = 170807
kode_rahasia = "17agustus"
print("\n================MENU ACCONT AZKY================\n")
print("\n1. ussername and password \n")
print("\n2.  pin atm \n")
print("\n3. cek ussername and password \n")

pilihan = input("mau pilih menu nomer berapa nih ? (1/2/3) ==>")



if pilihan == "1":
    percobaan = 3
    while percobaan >0 :
        ussername = input("masukkan ussername anda =")
        password = input("masukkan password anda = ")
        if ussername == ussername_benar and password == password_benar :
            print("login berhasil nihh azkyyy simanieez dan ganteng")
            break
        else:
            percobaan -= 1
            print("Password salahhh!!, sisa percobaan =", percobaan)
    if percobaan == 0:
        print("akun anda di blokirrr!!!")
elif pilihan == "2":
    percobaan = 3
    while percobaan >0:
        pin = int(input("masukkan pin atm anda = "))
        if pin == pin_benar :
            print("=====horeeeeee pin ATM azkii benarrr !!!=======\n")
            break
        else:
            percobaan -= 1
            print("Azkyyy , ko kamu bisa lupa sih pin atm Kamuu , hemm coba lagi ","sisa percobaan =", percobaan)
    if percobaan == 0:
        print("pin Atm kamu diblokir azkiii!!!")
elif pilihan == "3":
    percobaan = 2
    while percobaan >0:
        user = input("masukkan kode rahasiannya = ")
        if user == kode_rahasia:
            print("Nih, ussername kamu ===> ", ussername_benar)
            print("Passwordnya juga ====> ", password_benar)
            break
        else:
            percobaan -= 1
            print("yah salah kodenya, coba lagi nih , ", "sisa kesempatan ==>", percobaan)
    if percobaan == 0:
        print("wahhhh kamu gak bisa akses akun kamu ya !!!")
        print("Silahkan Hubungi kantor atm rekening kamu !!")
else:
    print("PILIHAN TIDAK VALID !!!!!")
        
        
    
    
    