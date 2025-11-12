import tempfile
import os

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_file.write(b'Counting my bytes!')
    temp_file.flush()
    temp_size = os.path.getsize(temp_file.name)
    print("Ukuran file sementara:", temp_size, "bytes")
# Fungsi: Menghitung ukuran dari file sementara.
# Kondisi: Ketika Anda perlu menganalisis ukuran file sementara.
