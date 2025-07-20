kalimat = input("Karakter = ").lower()
print("Huruf Konsonannya : ")


for huruf in kalimat:
    if huruf.isalpha() and huruf not in "aiueo":
        print(huruf , end= "")
