class StackUndo:
    def __init__(self):
        # List digunakan sebagai implementasi Stack
        self.stack = []

    def push(self, data):
        """Menyimpan kondisi sebelum perubahan."""
        self.stack.append(data)

    def pop(self):
        """Mengambil perubahan terakhir."""
        if self.is_empty():
            return None

        return self.stack.pop()

    def is_empty(self):
        """Mengecek apakah Stack kosong."""
        return len(self.stack) == 0

    def clear(self):
        """Menghapus seluruh riwayat Undo."""
        self.stack.clear()