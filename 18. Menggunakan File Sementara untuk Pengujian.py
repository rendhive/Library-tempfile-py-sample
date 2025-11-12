import tempfile

def test_tempfile_usage():
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(b'Temporary test data.')
        temp_file.seek(0)
        return temp_file.read()

print("Testing tempfile:", test_tempfile_usage())
# Fungsi: Menguji penggunaan file sementara dalam fungsi.
# Kondisi: Ketika Anda melakukan pengujian kode untuk memastikan fungsionalitas.
