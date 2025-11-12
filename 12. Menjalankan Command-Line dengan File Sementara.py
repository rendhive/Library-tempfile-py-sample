import tempfile
import subprocess

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_file.write(b'Hello from temp file!\n')
    temp_file.flush()  # Pastikan untuk flush sebelum menggunakan subprocess
    result = subprocess.run(['cat', temp_file.name], capture_output=True, text=True)
    print("Isi dari file sementara menggunakan subprocess:", result.stdout)
# Fungsi: Menyimpan data dalam file sementara dan membacanya menggunakan subprocess.
# Kondisi: Ketika Anda ingin mengalihkan data dari file sementara ke proses command-line.
