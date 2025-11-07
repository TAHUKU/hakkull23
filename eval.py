tinggi = int(input('masukan tinggi anak: '))
umur = int(input("masukan umur anak: "))
if tinggi >= 120:
    if umur >=12:
        status = 'silahkan masuk sendiri'
    else:
        status = 'boleh masuk asal di temani'
else:
    status = 'tinggi kurang, tidak boleh masuk'
print(f'tinggi anak anda {tinggi} cm \numur anda {umur} tahun \nstausnya: {status}')