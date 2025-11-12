import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    print("Direktori sementara dibuat:", temp_dir)
# Fungsi: Membuat direktori sementara yang akan dihapus setelah digunakan.
# Kondisi: Ketika Anda perlu menyimpan file temporer dalam struktur folder.
