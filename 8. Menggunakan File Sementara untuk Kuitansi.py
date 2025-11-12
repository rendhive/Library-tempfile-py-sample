import tempfile

with tempfile.NamedTemporaryFile(delete=True, mode='w+t') as temp_invoice:
    temp_invoice.write("Item: Book\nPrice: $10\n")
    temp_invoice.seek(0)
    print("Kuitansi:\n", temp_invoice.read())
# Fungsi: Mencetak kuitansi sementara menggunakan file sementara.
# Kondisi: Ketika Anda perlu menghasilkan kuitansi tanpa ingin menyimpannya secara permanen.
