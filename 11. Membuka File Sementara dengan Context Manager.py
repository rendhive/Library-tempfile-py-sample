import tempfile

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    with open(temp_file.name, 'w') as f:
        f.write("Data temporer")
    print("Data disimpan di file sementara:", temp_file.name)
# Fungsi: Menggunakan context manager untuk membuka file sementara.
# Kondisi: Ketika Anda ingin memastikan file dibuka dan ditutup dengan aman.
