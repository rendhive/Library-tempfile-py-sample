import tempfile

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_file.write(b'This is a temporary file.')
    temp_file.seek(0)
    print("Isi file sementara:", temp_file.read().decode())
# Fungsi: Menulis data ke file sementara dan membacanya.
# Kondisi: Ketika Anda perlu menyimpan sementara data yang akan segera digunakan.
