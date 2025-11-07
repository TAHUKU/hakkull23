nama = 'promo 20%'
print(nama)
belanja = int(input("masukan total belanja: "))
if belanja > 100000:
    diskon = belanja * 0.2
    total_bayar = belanja - diskon
    print(f'selamat anda mendapatkan diskon 20% yang awal harganya {belanja} \ndikarenakan dapat diskon menjadi: {total_bayar:.0f}')
else:
    total_bayar = belanja
    print("tidak dapat diskon, mohon maaf")
print(f"mohon bayar: Rp{total_bayar:.0f}")
uang = int(input("masukan uang yang anda miliki: "))
kembalian = (uang - total_bayar)
if uang == belanja:
    print('uang anda pas')
elif uang > belanja:
    print(f'terima kasih, uang kembailan anda: {kembalian:0f}')
else:
    print(f'uang anda kurang Rp: {kembalian:0f}, mohon di tambah')


