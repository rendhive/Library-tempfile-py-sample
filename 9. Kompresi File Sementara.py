import tempfile
import gzip

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    with gzip.GzipFile(file=temp_file.name, mode='wb') as f:
        f.write(b'This is a compressed temporary file.')
    with gzip.GzipFile(file=temp_file.name, mode='rb') as f:
        print("Isi file terkompresi:", f.read().decode())
# Fungsi: Menggunakan gzip untuk menulis dan membaca file sementara yang terkompresi.
# Kondisi: Ketika Anda perlu menyimpan data secara efisien menggunakan kompresi.
