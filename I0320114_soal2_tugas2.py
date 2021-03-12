# Buat Variabel

Nama = "Yukuri Hanjani Putri"
Nama_panggilan = "Yuku"
SMA = "SMA N 7 Yogyakarta"
Hobi = "Menggambar"
Jurusan = "Teknik Industri"
Institusi = "Universitas Sebelas Maret"
Idola = "Steve Jobs"

Tempat_lahir = "Bandar Lampung"
Alamat = "Bantul, Daerah Istimewa Yogyakarta"

Tinggi_badan = 165.6
Berat_badan = 60
Ukuran_sepatu = 40

Minuman_kesukaan = "Es Teh"
Makanan_kesukaan = "Magelangan"
Warna_kesukaan = "Biru"

# Tanggal, bulan, dan tahun lahir
TanggalLahir = 3
BulanLahir = 10            # 10 = Oktober
TahunLahir = 2001
TanggalSkrg = 11
BulanSkrg = 3
TahunSkrg = 2021

#Menghitung Usia (Tahun dan Bulan)
Usia_Dalam_Bulan = ((12 * TahunSkrg + BulanSkrg) - (12 * TahunLahir + BulanLahir))
Usia_Tahun = int(Usia_Dalam_Bulan/12)
Usia_Bulan = Usia_Dalam_Bulan % 12
Usia = str(Usia_Tahun) + " Tahun " + str(Usia_Bulan) + " Bulan"

#tampilan
print("==== BIODATA ====")
print("Nama :", Nama)
print("Usia :", Usia)
print("Nama Panggilan :", Nama_panggilan)
print("SMA :", SMA)
print("Hobi :", Hobi)
print("Jurusan :", Jurusan)
print("Institusi :", Institusi)
print("Idola :", Idola)
print("Tempat Lahir :", Tempat_lahir)
print("Alamat :", Alamat)
print("Tinggi Badan :", Tinggi_badan, "cm")
print("Berat Badan :", Berat_badan, "kg")
print("Ukuran Sepatu :", Ukuran_sepatu)
print("Makanan Kesukaan :", Makanan_kesukaan)
print("Minuman Kesukaan :", Minuman_kesukaan)
print("Warna Kesukaan :", Warna_kesukaan)