### Hitung Luas Persegi Panjang

# informasi program
print("===== Hitung Luas Persegi Panjang =====")

# input panjang dan lebar
panjang = float(input("Memasukan Panjang: "))
lebar = float(input("Memasukan Lebar: "))

# proses hitung luas
luasPersegiPanjang = panjang * lebar

# menampilkan hasil
print("Luas Persegi Panjang =", luasPersegiPanjang, "\n")

### Hitung Luas Lingkaran

# informasi program
print("===== Hitung Luas Lingkaran =====")

# input jari-jari
r = float(input("Memasukan Jari-Jari: "))

# proses hitung luas

luasLingkaran = 3.14 * (r ** 2)

# menampilkan hasil
print("Luas lingkaran =", luasLingkaran, "\n")

### Hitung Luas Kubus

# informasi program
print("===== Hitung Luas Kubus =====")

# input rusuk
s = float(input("Memasukan Panjang Rusuk: "))

# proses hitung luas
luasKubus = 6 * (s ** 2)

# menampilkan hasil
print("Luas kubus =", luasKubus, "\n")

### Menghitung konversi suhu celcius ke fahrenheit

# informasi program
print("===== Konversi suhu celcius ke fahrenheit =====")

# input celcius
celcius = float(input("Masukkan suhu celcius: "))

# proses hitung celcius ke fahrenheit
fahrenheit = (celcius * (9/5))+ 32

# menampilkan hasil
print(celcius, "celcius =", fahrenheit, "fahrenheit", "\n")

### Menghitung konversi suhu reamur ke kelvin

# informasi program
print("===== Konversi suhu reamur ke kelvin =====")

# input reamur
reamur = float(input("Masukkan suhu reamur: "))

# proses hitung celcius ke fahrenheit
kelvin = (reamur * (5/4)) + 273.15

# menampilkan hasil
print(reamur, "reamur =", kelvin, "kelvin")
