from data_mahasiswa import DataMahasiswa
from stack_undo import StackUndo
from queue_antrean import QueueAntrean
from hash_table import HashTableMahasiswa


class SistemAkademik:
    def __init__(self):
        # Membuat objek dari masing-masing struktur data
        self.data_mahasiswa = DataMahasiswa()
        self.stack_undo = StackUndo()
        self.queue_antrean = QueueAntrean()
        self.hash_table = HashTableMahasiswa()

        # Menyinkronkan data awal dengan Hash Table
        self.hash_table.sinkronisasi(
            self.data_mahasiswa.data
        )

    # ==========================================
    # DATA MAHASISWA
    # ==========================================

    def tampilkan_mahasiswa(self):
        self.data_mahasiswa.tampilkan()

    def tambah_mahasiswa(self):
        print("\n=== TAMBAH MAHASISWA ===")

        nim = input("NIM   : ").strip()

        # Cek apakah NIM sudah digunakan
        if self.hash_table.cari(nim):
            print("NIM sudah terdaftar.")
            return

        nama = input("Nama  : ").strip()
        prodi = input("Prodi : ").strip()

        mahasiswa_baru = {
            "nim": nim,
            "nama": nama,
            "prodi": prodi
        }

        # Simpan kondisi sebelum perubahan ke Stack
        kondisi_sebelumnya = self.data_mahasiswa.salin_data()
        self.stack_undo.push(kondisi_sebelumnya)

        # Tambahkan ke Array/List
        self.data_mahasiswa.tambah(mahasiswa_baru)

        # Tambahkan ke Hash Table
        self.hash_table.tambah(mahasiswa_baru)

        print("Mahasiswa berhasil ditambahkan.")

    def hapus_mahasiswa(self):
        print("\n=== HAPUS MAHASISWA ===")

        nim = input("Masukkan NIM yang ingin dihapus: ").strip()

        mahasiswa = self.hash_table.cari(nim)

        if mahasiswa is None:
            print("Mahasiswa tidak ditemukan.")
            return

        # Simpan kondisi sebelum perubahan ke Stack
        kondisi_sebelumnya = self.data_mahasiswa.salin_data()
        self.stack_undo.push(kondisi_sebelumnya)

        # Hapus dari Array/List
        self.data_mahasiswa.hapus(nim)

        # Hapus dari Hash Table
        self.hash_table.hapus(nim)

        print(
            f"Mahasiswa dengan NIM {nim} "
            f"berhasil dihapus."
        )

    # ==========================================
    # HASH TABLE
    # ==========================================

    def cari_mahasiswa(self):
        print("\n=== CARI MAHASISWA ===")

        nim = input("Masukkan NIM: ").strip()

        # Pencarian menggunakan Hash Table
        mahasiswa = self.hash_table.cari(nim)

        if mahasiswa is None:
            print("Data mahasiswa tidak ditemukan.")
            return

        print("\nData mahasiswa ditemukan:")
        print(f"NIM   : {mahasiswa['nim']}")
        print(f"Nama  : {mahasiswa['nama']}")
        print(f"Prodi : {mahasiswa['prodi']}")

    # ==========================================
    # STACK / UNDO
    # ==========================================

    def undo(self):
        print("\n=== UNDO ===")

        kondisi_sebelumnya = self.stack_undo.pop()

        if kondisi_sebelumnya is None:
            print("Tidak ada perubahan yang dapat dibatalkan.")
            return

        # Mengembalikan data mahasiswa
        self.data_mahasiswa.pulihkan(
            kondisi_sebelumnya
        )

        # Menyinkronkan kembali Hash Table
        self.hash_table.sinkronisasi(
            self.data_mahasiswa.data
        )

        print("Perubahan terakhir berhasil dibatalkan.")

    # ==========================================
    # QUEUE / ANTREAN
    # ==========================================

    def tambah_antrean(self):
        print("\n=== TAMBAH ANTREAN ===")

        nim = input("Masukkan NIM mahasiswa: ").strip()

        mahasiswa = self.hash_table.cari(nim)

        if mahasiswa is None:
            print("Mahasiswa tidak ditemukan.")
            return

        self.queue_antrean.enqueue(nim)

        print(
            f"Mahasiswa {mahasiswa['nama']} "
            f"berhasil masuk ke antrean."
        )

    def tampilkan_antrean(self):
        self.queue_antrean.tampilkan()

    def proses_antrean(self):
        print("\n=== PROSES ANTREAN ===")

        nim = self.queue_antrean.dequeue()

        if nim is None:
            print("Tidak ada mahasiswa dalam antrean.")
            return

        mahasiswa = self.hash_table.cari(nim)

        print("Antrean sedang diproses.")
        print(f"NIM   : {mahasiswa['nim']}")
        print(f"Nama  : {mahasiswa['nama']}")
        print(f"Prodi : {mahasiswa['prodi']}")
        print("Status: Permintaan selesai diproses.")

    # ==========================================
    # MENU UTAMA
    # ==========================================

    def tampilkan_menu(self):
        print("\n======================================")
        print("       SISTEM AKADEMIK MAHASISWA")
        print("======================================")
        print("1. Tampilkan data mahasiswa")
        print("2. Tambah mahasiswa")
        print("3. Hapus mahasiswa")
        print("4. Cari mahasiswa berdasarkan NIM")
        print("5. Undo perubahan terakhir")
        print("6. Tambah mahasiswa ke antrean")
        print("7. Tampilkan antrean")
        print("8. Proses antrean")
        print("9. Keluar")
        print("======================================")

    def jalankan(self):
        while True:
            self.tampilkan_menu()

            pilihan = input("Pilih menu (1-9): ").strip()

            if pilihan == "1":
                self.tampilkan_mahasiswa()

            elif pilihan == "2":
                self.tambah_mahasiswa()

            elif pilihan == "3":
                self.hapus_mahasiswa()

            elif pilihan == "4":
                self.cari_mahasiswa()

            elif pilihan == "5":
                self.undo()

            elif pilihan == "6":
                self.tambah_antrean()

            elif pilihan == "7":
                self.tampilkan_antrean()

            elif pilihan == "8":
                self.proses_antrean()

            elif pilihan == "9":
                print("\nProgram selesai. Terima kasih.")
                break

            else:
                print("\nPilihan tidak tersedia.")

            input("\nTekan Enter untuk kembali ke menu...")


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================

if __name__ == "__main__":
    sistem = SistemAkademik()
    sistem.jalankan()