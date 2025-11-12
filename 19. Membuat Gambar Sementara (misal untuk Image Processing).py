import tempfile
from PIL import Image
import numpy as np

with tempfile.NamedTemporaryFile(delete=True, suffix='.png') as temp_file:
    img_array = np.zeros((100, 100, 3), dtype=np.uint8)
    image = Image.fromarray(img_array)
    image.save(temp_file.name)
    print("Gambar disimpan sementara di:", temp_file.name)
# Fungsi: Membuat gambar sementara menggunakan pillow.
# Kondisi: Ketika Anda ingin melakukan pemrosesan gambar tanpa menyimpan secara permanen.
