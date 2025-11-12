import tempfile

temp_file = tempfile.NamedTemporaryFile(delete=False)
print("File sementara yang tidak akan dihapus:", temp_file.name)
temp_file.close()  # Pastikan file ditutup sebelum dipindahkan
# Fungsi: Membuat file sementara yang tidak dihapus otomatis saat ditutup.
# Kondisi: Saat Anda perlu mempertahankan file untuk penggunaan pasca skrip.
