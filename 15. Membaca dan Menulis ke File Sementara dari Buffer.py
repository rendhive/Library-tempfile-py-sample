import tempfile
import io

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_buffer = io.StringIO('Data dari buffer temporal.')
    temp_file.write(temp_buffer.getvalue().encode())
    temp_file.seek(0)
    print("Isi file sementara dari buffer:", temp_file.read().decode())
# Fungsi: Menggunakan buffer untuk menulis data ke file sementara.
# Kondisi: Ketika data awalnya disimpan dalam objek buffer dan harus ditulis ke file.
