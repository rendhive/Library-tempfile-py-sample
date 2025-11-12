import tempfile

def write_temp_file(content):
    with tempfile.NamedTemporaryFile(delete=True, mode='w+t') as temp_file:
        temp_file.write(content)
        temp_file.seek(0)
        return temp_file.read()

print("Isi file sementara dari fungsi:", write_temp_file("Temporary Data"))
# Fungsi: Menggunakan file sementara dalam fungsi untuk menyimpan data.
# Kondisi: Ketika Anda ingin membungkus logika pembuatan file sementara ke dalam fungsi.
