totalBelanja = int(input("masukan total belanja: "))

if totalBelanja > 100000:
    discound = totalBelanja * 0.2
    total_bayar = totalBelanja - discound
    print(f'selamat anda dapat discound 20% \nyang harga awal: Rp{totalBelanja} \nmenjadi: Rp.{total_bayar:.0f}')
elif totalBelanja == 100000:
    discound = 0
    total_bayar = totalBelanja - discound
    print(f'belum beruntung, jika ingin mendapatkan diskon belanja lebih dari 100000')
else:
    discound = 0
    total_bayar = totalBelanja
    print("Belanja anda kurang dari 100.000, belum bisa dapat diskon" )
    
print(f'jumlah yang harus anda bayar adalah Rp.{total_bayar:.0f}')

masukanUang = int(input("masukan uang anda: "))
kembalian = masukanUang - total_bayar
kekurangan = total_bayar - masukanUang

if masukanUang > total_bayar:
    status = f'uang anda lebih kembalian anda: {kembalian:.0f} 😁'
elif masukanUang < total_bayar:
    status = f'mohon maaf uang anda kurang {kekurangan:.0f}. mohon di tambah 😊'
else:
     status = f'uang anda pas, Terima kasih 🙏🏻'
print("\n=======Struk Transaksi======")
print(f"total belanja            : {totalBelanja}")
print(f"total bayar              : {total_bayar:.0f}")
print(f"uang yang di berikan     : {masukanUang}")
if masukanUang >= total_bayar:
    print(f'kembalian       : {kembalian:.0f}')
print(status)
print("=========Terima kasih=========") 