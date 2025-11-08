kata = input("masukan kata: ")
cari = input("masukan huruf yang dicari: ")

for huruf in kata:
    if huruf == cari:
        print("huruf", cari, "di temukan dalam kata")
        break
    else:
        print("huruf", cari, "tidak ada dalam kata")