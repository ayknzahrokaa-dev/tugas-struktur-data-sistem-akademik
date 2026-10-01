class HashTableMahasiswa:
    def __init__(self):
        # Dictionary digunakan sebagai implementasi Hash Table
        self.table = {}

    def tambah(self, mahasiswa):
        """Menyimpan mahasiswa menggunakan NIM sebagai key."""
        nim = mahasiswa["nim"]
        self.table[nim] = mahasiswa

    def cari(self, nim):
        """Mencari mahasiswa berdasarkan NIM sebagai key."""
        return self.table.get(nim)

    def hapus(self, nim):
        """Menghapus mahasiswa berdasarkan NIM."""
        if nim in self.table:
            del self.table[nim]

    def sinkronisasi(self, data_mahasiswa):
        """Menyamakan isi Hash Table dengan data mahasiswa."""
        self.table.clear()

        for mahasiswa in data_mahasiswa:
            self.tambah(mahasiswa)