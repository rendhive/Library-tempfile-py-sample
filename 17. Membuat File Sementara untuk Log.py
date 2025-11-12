import tempfile
import logging

logging.basicConfig(filename=tempfile.mktemp(), level=logging.DEBUG)
logging.debug('This is a log message.')
print("Log telah ditulis ke file sementara.")
# Fungsi: Membuat file log sementara.
# Kondisi: Ketika Anda membutuhkan log sementara tanpa menyimpannya secara permanen.
