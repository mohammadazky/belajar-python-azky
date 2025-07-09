umur = int(input("masukkan umur anda = "))
if umur >=0 and umur <= 12:
    print("Anda masih anak anak")
elif umur >= 12 and umur <= 17:
    print("ANDA REMAJA")
elif umur >= 18 and umur <= 59:
    print("Anda dewasa")
else:
    print("anda lansia")