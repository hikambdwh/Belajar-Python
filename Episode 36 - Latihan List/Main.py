# program list buku

list_buku = []
while True:
	print("\nMasukan data buku")
	judul = input("Judul buku\t: ")
	penulis = input("Nama penulis\t: ")
	tahun = int(input("tahun terbit\t: "))

	buku_baru = [judul,penulis,tahun]
	list_buku.append(buku_baru)
	print(list_buku)
	print(list_buku[0])
	print("\n\n","="*10,"Data Buku","="*10)
	for index,buku in enumerate(list_buku):
		print(f"{index+1} | {buku[0]} | {buku[1]} ({buku[2]})")
	
	print("\n\n","="*20)
	isLanjut = input("Apakah dilanjutkan?(y/n) ")

	if isLanjut == "n":
		break

print("PROGRAM SELESAI")