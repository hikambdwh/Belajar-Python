# Perulangan (loop)

# for kondisi:
# 	aksi

# ini dengan list
angka2_list = [0,2,4,8,10] # ini adalah list
print(angka2_list)

for i in angka2_list:
	print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
	print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")

angka2_range = range(1,10)

for i in angka2_range:
	print(f"i sekarang -> {i}")
	# print("saya keren")

print("akhir dari program 3 \n")

# menggunakan string

data_str = "saya ganteng abiees"

for huruf in data_str:
	print(huruf)

print("akhir dari program 4 \n")


for i in range(0, 8, 1):
    for j in range(0, i, 1):
        print("*", end="")  # mencetak di baris yang sama
    print()  # ganti baris


for i in range(7,0, -1):
	for j in range(i-1,0,-1):
		print(" ", end="")
	for k in range(8,i,-1):
		print("*", end="")
	print()
	
bintang = 7
for i in range(0,bintang):
	for j in range(0,i):
		print(" ", end="")
	for k in range(bintang,i,-1):
		print("*", end="")
	print()
