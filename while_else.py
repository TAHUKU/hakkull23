password_true = "sayangggg"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("masukan password: ")
    percobaan += 1

    if password == password_true:
        print("login aman")
        break
    else:
        print("pswd salah, sisah percobaan", max_percobaan)
else:
    print("terlalu banyak percobaan. login gagal")