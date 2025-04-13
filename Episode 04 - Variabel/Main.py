# Variabel adalah tempat menyimpan data

# menaru / assignment nilai
a = 10
x = 5
panjang = 1000
panjangBool = bool(panjang)

# pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)
print(f"panjang {panjangBool}")

# penamaan
nilai_y = 15 # dengan menggunakan underscore
juta10 = 10000000 # ini boleh
nilaiZ = 17.5 # ini boleh

# pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

# assignment indirect
b = a
print("Nilai b = ", b)