print("mencetak angka 1-5")
angka = 1
while angka <= 5:
    print(angka)
    angka += 1

#Input sampai benar
password = ""
while password != "tahuku23":
    password = input("masukan password: ")
    if password != "tahuku23":
        print("pswd salah, try again")

print("pasword benar")