while True:
    try:
        angka = int(input("masukan bilangan genap: "))
        if angka % 2 == 0:
            print(f"angka genap di terima {angka}")
            break
        else:
            print(f"bukan angka genap {angka} masukan angka lagi")
        continue   
    except ValueError:
        print("input ini bukan angka. try again")
        continue


