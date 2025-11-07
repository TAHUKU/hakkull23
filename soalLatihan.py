# Jelaskan perbedaan antara indexing dan slicing pada string. Sertakan contoh kode Python.
indexing_slicing = " Jelaskan perbedaan antara indexing dan slicing pada string. Sertakan contoh kode Python."
nama = "hakkull"
print(f'contoh indexing: {nama}')
print(nama[0]) 
print(nama[1])
print(nama[2])
print(nama[3])
print(nama[4])
print(nama[5])
print(nama[6])
nama = "hakkull"
print(f'contoh slicing: {nama}')
print(nama[0:3]) #print huruf dari awal huruf 
print(nama[2:4]) #print huruf dari awal huruf ke 2 sampai 4 / ()
kesimpulan = "perbedaan antara indexing dan slicing adalah... \nindexing yaitu mengakses per karakter \nsedangkan slicing untuk mengambil sebagian dari text"
print(f"jadi: {kesimpulan} \n")
# Apa kegunaan dari method strip() dan replace() pada string? Berikan contoh penggunaannya.
latian = "Apa kegunaan dari method strip() dan replace() pada string? Berikan contoh penggunaannya"
print(latian)
nama = "                hakkull              "
kalimat = "dia milikmu"
nama_strip = nama.strip()
kalimat_baru =  kalimat.replace("milikmu", "milikku")
print(f'nama sebelum di kasi method strip(): {nama} \nnama yang sudah dikasi strip(): {nama_strip} \nkalimat sebelum di repleace: {kalimat} \nkalimat yang sudah dikasi repleace(): {kalimat_baru} \n')
# Bagaimana cara menulis string yang mengandung tanda kutip ganda (") di dalamnya? Berikan 2 cara berbeda.
string =  "Bagaimana cara menulis string yang mengandung tanda kutip ganda ("") di dalamnya? Berikan 2 cara berbeda."
print(f"{string} sek eror... otak mungilku gak ngatasi\n")
text = 'hari ini saya belajar type string'
print(text)
tex = "besok saya belajar int"
print(tex)
# Tuliskan contoh penggunaan f-string yang melibatkan ekspresi matematika
fstring = "Tuliskan contoh penggunaan f-string yang melibatkan ekspresi matematika"
print(fstring)
mtk1 = 50000
mtk2 = 60000
hasil = mtk1 + mtk2



print(f"hasil dari mtk1 + mtk2 adalah: {mtk1} + {mtk2} = {hasil} ")


