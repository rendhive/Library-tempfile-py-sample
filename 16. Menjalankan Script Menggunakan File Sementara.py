import tempfile
import subprocess

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    temp_file.write(b'print("Hello from temporary script!")\n')
    temp_file.flush()  # Pastikan data ditulis
    subprocess.run(['python3', temp_file.name])
# Fungsi: Menjalankan script Python sementara yang ditulis ke file.
# Kondisi: Ketika Anda ingin mengeksekusi kode Python yang dinamis.
