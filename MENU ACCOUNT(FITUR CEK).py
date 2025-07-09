from datetime import datetime
import time



username_benar = "baskaralangit1"
password_benar = "Baskaralangit"
pin_benar = 456123
kode_akses = 20070817
nama= "Bagaskaralangit"

def cek_username(user_input):
    if not user_input.isalnum():
        return False, "Username harus Berbentuk Huruf dan karakter maniezz!"
    if len(user_input) > len (username_benar):
        return False, "Karakter Yang Anda Input Melebihi Username Yang Didaftarkan!"
    if user_input != username_benar:
        return False, "username salah!! manieeezz coba lagi ya"
    return True, "Username benarrr! "

def cek_password(pw_input):
    if not pw_input.isalnum():
        return False, "Password Harus Berbentuk Huruf dan Karakter Maniezz"
    if len(pw_input) > len (password_benar):
        return False, "Password Yang Anda Masukkan Terlalu melebihi Password Yang Anda Daftarkan!"
    if pw_input != password_benar:
        return False, "Password Salahh!, Maniss Coba Lagi ya!!"
    return True, "Horeeeee maniezzz Passwordnya Benar!"
def cek_pin (pin_input):
    try:
        pin = int(pin_input)
    except ValueError:
        return False, "Pin Yang Anda Masukkan Bukan Angka Sepenuhnya!!"
    if pin != pin_benar:
        return False, "Pin salah!!! Coba Masukkin Pin Yang Benar"
    return True, "PIN BENARRR ! HORE MANIEZZZ"

def logout ():
    print("Anda Telah Keluar Dari Menu Account Maniezzz")
    print(f"Terima Kasih Telah Menjaga Akun Anda Dengan Baik Maniezz {nama}")
    print("------------SELAMAT BAHAGIA TERUS--------------------")
    return

def login_account():
    for b in range(3):
        user = input("Username ANDA = ")
        status, pesan = cek_username(user)
        print(pesan)
        time.sleep(0.5)
        if not status:
            print(f"sesi mencoba memasukkan ussername yang didaftarkan ! sesi coba lagi tersisa {2-b}")
            continue
        for a in range(3):
            pw= input("Password ANDA =")
            status_pw, pesan_pw = cek_password(pw)
            print(pesan_pw)
            time.sleep(0.5)
            if not status_pw:
                print(f"Password Anda Tidak Sesuai Dengan Yang Didaftarkan Sisa Percobaan Tersisa {2-a}")
                continue
            for j in range(3):
                pin= input("PIN ATM (UNTUK MEMBUKA AKSES LOGIN ) = ")
                status_pin, pesan_pin = cek_pin(pin)
                print(pesan_pin)
                time.sleep(0.5)
                if not status_pin:
                    print(f"Pin tidak sesuai! sisa percobaan = {2-j}")
                    continue

                print("\nLogin Berhasil!, jaga terus ya data accountnya\n")
                print("\nTANGGAL LOGIN = ", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
                logout()
            print("PIN SALAH 3 KALI !!! AKSES ANDA DIBLOKIR!")
            return False
        print("Password 3 kali Salahh!! Akses Diblokir!")
        return False
    print("Username Salah 3 kali!! Akses Anda Diblokir Tidak Bisa Login!!")
    return False

def cek_data_account():
    percobaan = 3
    while percobaan > 0:
        try:
            kode=int(input("Masukkan Kode Akses(MEMBUKA DATA ACCOUNT) = "))
        except ValueError:
            print("Manieeezz!! Masukkan Kodenya Berupa Angka Ya!!")
            percobaan -= 1
            continue
        if len(str(kode)) > len(str(kode_akses)):
            print("Kode Terlalu Panjang!!!! Masukkan Sesuai Kode Akses Yang Anda Buat!")
            print(f"SISA PERCOBAAN {percobaan}")
            percobaan-= 1
            continue

        if kode == kode_akses:
            print("\n==================DATA ACCOUNT ANDA==============\n")
            print(f"Nama Anda =  {nama}")
            print(f"Username Anda = {username_benar}")
            print(f"Password Anda = {password_benar}")
            print(f"Pin ATM Anda = {pin_benar}")
            print(f"Kode Rahasia Membuka Data = {kode_akses}")
            print("--------Jaga Terus Ya Data INI manieezz----------------")
            print("------Terima-kasih Telah Menjadi Bagian Bank Ini-----")
            logout()
            return
        else:
            percobaan -= 1
            print(f"Kode Salah!!! sesi percobaan memasukkan kode {percobaan}")
    print("kode Akses Ditolak!! Sudah Lewat 3 kali")
    return False
def main_menu():
    while True:
        print("\n=====================BANK AZKI KAMIL=================\n")
        print("1. LOGIN UTAMA")
        print("2. CEK DATA ACCOUNT TERDAFTAR")
        print("3. KELUAR")

        pilihan = input("Pilih Menu MANIEZZZ (1/2/3) = ")

        if pilihan == "1":
            login_account()
        elif pilihan == "2":
            cek_data_account()
        elif pilihan == "3":
            print("Sampai jumpa lagi, manieezz!")
            break
        else:
            print("PILIHAN TIDAK VALID!!! Hanya 1-3 MENU YA MANIEEZ!")


main_menu()

        
        

                

    
        
