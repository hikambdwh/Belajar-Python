class Mahasiswa():
	nama = 'nama'
	nim = 2300798

otong = Mahasiswa()
ucup = Mahasiswa()

otong.nama = "otong surotong"
otong.nim = 2300777
ucup.nama = "michael ucup"
ucup.nim = 2300989

print(f"""
	Nama: {otong.nama}	
	NIM:  {otong.nim}
""")
print(f"""
	Nama: {ucup.nama}	
	NIM:  {ucup.nim}
""")

