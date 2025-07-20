while True:
    try:
        nilai = int(input("masukkan nilai = "))
        if nilai >= 90:
            print("nilai anda A")
            break
        elif nilai >=80 and nilai <=89:
            print("Nilai Anda B")
            break
        elif nilai >= 70 and nilai <=79:
            print("Nilai Anda C")
            break
        else:
            print("nilai anda D")
            break
    except ValueError:
        print("Nilai Itu Angka Kan? Bukan Huruf/karakter !!!")
        continue
