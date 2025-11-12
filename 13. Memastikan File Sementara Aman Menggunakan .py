import tempfile

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_file.write(b'Some temporary secure data.')
    temp_file.flush()
    print(f"File sementara '{temp_file.name}' aman digunakan.") 
# Fungsi: Menyimpan data sementara dan memastikan keamanannya.
# Kondisi: Ketika keamanan data sementara menjadi perhatian.
