import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    temp_file_path = f"{temp_dir}/temp_file.txt"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("Hello, Temporary World!")
    with open(temp_file_path, 'r') as temp_file:
        print("Isi file dalam direktori sementara:", temp_file.read())
# Fungsi: Menyimpan dan membaca file dari dalam direktori sementara.
# Kondisi: Ketika Anda ingin mengorganisir file temporer dalam folder.
