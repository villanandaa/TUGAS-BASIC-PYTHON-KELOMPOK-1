import csv
import os

class Tugas:
    def __init__(self, namafile="tugas.csv"):
        self.namafile = namafile
        self.list_tugas = []
        self.load_tugas()

    def load_tugas(self):
        try:
            with open(self.namafile, 'r') as file:
                reader = csv.reader(file)
                self.list = list(reader)
        except FileNotFoundError:
            # Jika file tidak ditemukan, buat file baru
            with open(self.namafile, 'w' ) as file:
                pass

    def simpan_tugas(self):
        with open(self.namafile, 'w' ) as file:
            writer = csv.writer(file)
            writer.writerows(self.list_tugas)

    def tambah_tugas(self, deskripsi, status="belum selesai"):
        self.list_tugas.append([deskripsi, status])
        self.simpan_tugas()
        print("Tugas berhasil ditambahkan.")
        input('Press Enter to continue...')
        os.system('cls')

    def display_tugas(self):
        if not self.list_tugas:
            print("Tidak ada tugas.")
        else:
            for i, tugas in enumerate(self.list_tugas, start=1):
                print(f"{i}. Deskripsi: {tugas[0]}, Status: {tugas[1]}")
            input('Press Enter to continue...')
            os.system('cls')

    def delete_tugas(self, task_index):
        try:
            del self.list_tugas[task_index - 1]
            self.simpan_tugas()
            print("Tugas berhasil dihapus.")
            input('Press Enter to continue...')
            os.system('cls')
        except IndexError:
            print("Indeks tugas tidak valid.")

task_manager = Tugas()

while True:
    os.system('cls')
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    choice = input("Pilih menu (1/2/3/4): ")

    if choice == '1':
        os.system('cls')
        description = input("Masukkan deskripsi tugas: ")
        task_manager.tambah_tugas(description)
    elif choice == '2':
        os.system('cls')
        task_manager.display_tugas()
    elif choice == '3':
        os.system('cls')
        task_manager.display_tugas()
        task_index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        task_manager.delete_tugas(task_index)
    elif choice == '4':
        print("Terimakasi, Sampai Jumpa!!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")