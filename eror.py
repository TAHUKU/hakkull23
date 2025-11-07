#variabel input data diri 
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
email_kampus = input("Masukkan email kampus Anda (Jawab dengan True/False): ")
#konversi tipe data
umur = int(umur)
email_kampus = bool(email_kampus == 'True')
#logika
if email_kampus == True and umur >= 17:
    status = "sudah memiliki email kampus dan diterima"
else:
    status = "belum memiliki email kampus dan belum diterima"
#output
print("==============Sistem pendaftaran mahasiswa baru========================")
print(f"Nama: {nama}  \nUmur: {umur} tahun \nApakah anda memiliki email kampus: {email_kampus}  \nStatus {nama}: {status}")
