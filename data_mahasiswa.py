class DataMahasiswa:
    def __init__(self):
        # Array/List untuk menyimpan data mahasiswa secara berurutan
        self.data = [
            {
                "nim": "231001",
                "nama": "Ahmad",
                "prodi": "Teknik Informatika"
            },
            {
                "nim": "231002",
                "nama": "Siti",
                "prodi": "Teknik Informatika"
            },
            {
                "nim": "231003",
                "nama": "Budi",
                "prodi": "Teknik Informatika"
            }
        ]

    def tampilkan(self):
        """Menampilkan seluruh data mahasiswa."""
        if not self.data:
            print("\nBelum ada data mahasiswa.")
            return

        print("\n=== DATA MAHASISWA ===")

        for nomor, mahasiswa in enumerate(self.data, start=1):
            print(
                f"{nomor}. "
                f"NIM: {mahasiswa['nim']} | "
                f"Nama: {mahasiswa['nama']} | "
                f"Prodi: {mahasiswa['prodi']}"
            )

    def tambah(self, mahasiswa):
        """Menambahkan mahasiswa ke dalam list."""
        self.data.append(mahasiswa)

    def hapus(self, nim):
        """Menghapus mahasiswa berdasarkan NIM."""
        for mahasiswa in self.data:
            if mahasiswa["nim"] == nim:
                self.data.remove(mahasiswa)
                return mahasiswa

        return None

    def cari(self, nim):
        """Mencari mahasiswa berdasarkan NIM."""
        for mahasiswa in self.data:
            if mahasiswa["nim"] == nim:
                return mahasiswa

        return None

    def salin_data(self):
        """Membuat salinan data untuk kebutuhan Undo."""
        return [mahasiswa.copy() for mahasiswa in self.data]

    def pulihkan(self, data_lama):
        """Mengembalikan data ke kondisi sebelumnya."""
        self.data = [mahasiswa.copy() for mahasiswa in data_lama]