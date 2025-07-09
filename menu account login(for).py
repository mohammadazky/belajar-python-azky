from datetime import datetime
import time



ussername_benar = "Mohammad_azky12"
password_benar = "Tasikmalayamaniez"
pin_benar = 20070807
kode_akses = 170807
nama = "mohammadazkykameel"

print("\n=============ACCOUNT BANK===========\n")
print("\n1. login account bank \n")
print("\n2. cek data account")


pilihan = input("Mau Menu yang mana nih manieezzz => (1/2) = ")

 
if pilihan == "1":
    for a in range(3):
        userr= input("Ussername kamu manieez = ")
        time.sleep(0.5)
        if userr == ussername_benar :
            print("Ussername benar nih manieez")
            time.sleep(0.5)

            for u in range(3):
                pw = input("Password manieez = ")
                time.sleep(0.5)
                if pw == password_benar :
                    print("Passwordnya Benarr nihh manieezz ! jangan sampai lupa ya !")
                    time.sleep(0.5)
                    for j in range(3):
                        pin = int(input("PIN REKENING KAMU = "))
                        time.sleep(0.5)
                        if pin == pin_benar:
                                print("PIN BENAR !")
                                time.sleep(0.5)
                                print("LOGINN BERHASIL ! JAGA TERUS YA MANIEEZ DATA ACCOUNTNYA")
                                print(" Tanggal login:", datetime.now().strftime("%d-%m-%Y  %H: %M: %S"))
                                exit()
                        else:
                            print(f"Salah! sisa percobaan = {2-j}")
                            time.sleep(0.5)
                    print("Pin Salahh 3kali!, akses diblokir!")
                    exit()   
                    
                else:
                    print(f"Password salah! Sisa percobaan {2-u}")
                    time.sleep(0.5)
            print("Password Salah OON 3kali!, tidak dapat login ! mohon hampura!")
            exit()
        else:
            print(f"Ussername Salah!!! sisa percobaan {2-a}")
            time.sleep(0.5)
    print("Ussername 3 kali salahh!, Akses ditolak oon!")
elif pilihan == "2":
    percobaan = 3
    while percobaan >0:
        kode= int(input("Masukkan Kode Akses Anda ="))
        if kode == kode_akses:
            print("\n===================Data Account Anda==============\n")
            print(f"Hallo {nama} Selamat Bahagia Tuan! Ini Data Account Anda =")
            print(f"Ussername Anda = {ussername_benar} ")
            print(f"Password Anda = {password_benar}")
            print(f"Pin ATM anda = {pin_benar}")
            print("-------------------------------------------------------")
            break
        else:
            percobaan -= 1
            print(f"Kode Akses Salah manieeezz!! sisa percobaan Atas Nama {nama} Tinggal Sisa = {percobaan}")
            time.sleep(0.5)
    if percobaan == 0:
        print("\n3 KALI SALAH!!! AKSES DIBLOKIRRRR!\n")
        print("-------Silahkan Hubungi Pihak Bank Terkait , TerimaKasih----------")



   
            