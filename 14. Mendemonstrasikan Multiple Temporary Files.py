import tempfile

for _ in range(3):
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        print("File sementara dibuat:", temp_file.name)
# Fungsi: Membuat beberapa file sementara.
# Kondisi: Ketika Anda membutuhkan beberapa file untuk operasi terpisah.
