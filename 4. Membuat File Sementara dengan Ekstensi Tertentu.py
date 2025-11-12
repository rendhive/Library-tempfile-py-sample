import tempfile

with tempfile.NamedTemporaryFile(suffix='.txt', delete=True) as temp_file:
    print("File sementara dengan ekstensi .txt dibuat:", temp_file.name)
# Fungsi: Membuat file sementara dengan ekstensi tertentu.
# Kondisi: Ketika Anda ingin memastikan format file tertentu.
