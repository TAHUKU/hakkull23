# To-Do List Sederhana

# List untuk menyimpan tugas
todo_list = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Lihat semua tugas")
    print("2. Tambah tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Keluar")

def lihat_tugas():
    if not todo_list:
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(todo_list, start=1):
            status = "✅" if tugas['selesai'] else "❌"
            print(f"{i}. {tugas['nama']} [{status}]")

def tambah_tugas():
    nama_tugas = input("Masukkan nama tugas: ")
    todo_list.append({'nama': nama_tugas, 'selesai': False})
    print("Tugas berhasil ditambahkan!")

def tandai_selesai():
    lihat_tugas()
    if todo_list:
        try:
            nomor = int(input("Masukkan nomor tugas yang selesai: "))
            if 1 <= nomor <= len(todo_list):
                todo_list[nomor - 1]['selesai'] = True
                print("Tugas telah ditandai selesai!")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

def hapus_tugas():
    lihat_tugas()
    if todo_list:
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(todo_list):
                tugas_hapus = todo_list.pop(nomor - 1)
                print(f"Tugas '{tugas_hapus['nama']}' berhasil dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

# Loop utama
while True:
    show_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        lihat_tugas()
    elif pilihan == '2':
        tambah_tugas()
    elif pilihan == '3':
        tandai_selesai()
    elif pilihan == '4':
        hapus_tugas()
    elif pilihan == '5':
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
