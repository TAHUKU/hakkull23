#game tebak angka dengan break
angka = 5
while True:
    tebak = int(input("tebak angka (1-10): "))
    if tebak == angka:
        print("selmat benar")
        break
    else:
        print("salah, try again")