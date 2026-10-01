from collections import deque


class QueueAntrean:
    def __init__(self):
        # deque digunakan sebagai implementasi Queue
        self.queue = deque()

    def enqueue(self, nim):
        """Menambahkan NIM ke belakang antrean."""
        self.queue.append(nim)

    def dequeue(self):
        """Mengambil NIM dari depan antrean."""
        if self.is_empty():
            return None

        return self.queue.popleft()

    def is_empty(self):
        """Mengecek apakah antrean kosong."""
        return len(self.queue) == 0

    def tampilkan(self):
        """Menampilkan isi antrean."""
        if self.is_empty():
            print("\nAntrean masih kosong.")
            return

        print("\n=== ANTREAN MAHASISWA ===")

        for nomor, nim in enumerate(self.queue, start=1):
            print(f"{nomor}. NIM: {nim}")