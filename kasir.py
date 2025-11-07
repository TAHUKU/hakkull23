orderNo = input("Masukkan Nomor Orderan: ")
tanggal = input("Tanggal Belanja (dd-mm-yyyy): ")
cashier = "Hakkul"

menu = input("Masukkan menu yang anda inginkan: ")
beli_berapa = int(input("Mau beli berapa: "))
harga_satuan = 10000  # harga per menu

# Hitung total harga
total = beli_berapa * harga_satuan

# Jika beli lebih dari 2, dapat diskon 10%
if beli_berapa > 2:
    diskon = total * 0.1
    total -= diskon
    print(f"\nAnda mendapat diskon 10%! Total setelah diskon: Rp{total:,}")
else:
    print(f"\nTotal pesanan anda: Rp{total:,}")

# Cetak struk
print("\n======= STRUK PEMBELIAN =======")
print(f"Nomor Orderan : {orderNo}")
print(f"Tanggal        : {tanggal}")
print(f"Kasir          : {cashier}")
print(f"Menu           : {menu}")
print(f"Jumlah Beli    : {beli_berapa}")
print(f"Harga Satuan   : Rp{harga_satuan:,}")
print(f"Total Bayar    : Rp{total:,}")
print("================================")
print("Terima kasih sudah belanja 🙏🏻")
