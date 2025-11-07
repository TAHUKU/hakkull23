# Anak hanya boleh masuk jika tingginya ≥ 120 cm.
# Jika tinggi memenuhi, cek lagi:
# Kalau umur ≥ 12 tahun, boleh masuk sendiri.
# Kalau umur < 12, hanya boleh masuk kalau ditemani orang tua.
# Jika tinggi kurang dari 120 cm → otomatis ditolak.

tinggi = int(input("Masukan tinggi anak: "))
umur = int(input("masukan umur anak: "))
if tinggi >= 120:
    status = 'boleh masuk'
    if umur >= 12:
        status = 'silahkan masuk sendiri'
        if umur < 12:
            status = 'boleh asal di temani'
else:
    status = 'mohon maaf tinggi kurang'
print(f'tinggi anak anda {tinggi} \numur anak anda {umur} \n{status}')