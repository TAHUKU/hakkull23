nama = input("masukan nama anda: ")
umur = int(input("Masukan umur anda: "))
email_kampus = input("Apakah anda suadah memiliki email kampus (Jawab True/False): ")
email_kampus = bool(email_kampus == 'True')
if email_kampus == True and umur >= 18:
    status = "Sudah memiliki emai kampus dan di terima"
else:
    status = "Belum memiliki email kampus dan belum di terima"

print(f"nama {nama} \numur {umur} tahun \nApakah anda memiliki email kampus: {email_kampus} \nStatus {nama}: {status}")