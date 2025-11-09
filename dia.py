while True: 
    try:
        angka = int(input("Masukkan bilangan genap: "))
    except ValueError:
        print("Input bukan angka. Silakan coba lagi.")
        continue

    if angka % 2 == 0:
        print(f"Terima kasih! Anda memasukkan bilangan genap: {angka}")
        break
    else:
        print("Angka ganjil. Silakan coba lagi.")