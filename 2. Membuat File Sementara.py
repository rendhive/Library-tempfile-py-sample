import tempfile

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    print("File sementara dibuat:", temp_file.name)
    
# Fungsi: Membuat file sementara yang secara otomatis dihapus setelah ditutup.
# Kondisi: Ketika Anda perlu menyimpan data sementara tanpa kekhawatiran tentang penghapusan manual.
