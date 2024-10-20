# Input pengeluaran dari pengguna
pengeluaran_satuminggu = float(input("Masukkan jumlah pengeluaran Satu minggu: "))
# Menentukan kategori berdasarkan jumlah pengeluaran Satu minggu
if pengeluaran_satuminggu < 200000:
    kategori = "Rendah"
elif pengeluaran_satuminggu < 300000:
    kategori = "Sedang"
elif pengeluaran_satuminggu < 500000:
    kategori = "Tinggi"
else:
    kategori = "Sangat Tinggi"
# Menampilkan hasil
print(f"Pengeluaran sebesar Rp{pengeluaran_satuminggu:.2f} termasuk dalam kategori {kategori}.")
