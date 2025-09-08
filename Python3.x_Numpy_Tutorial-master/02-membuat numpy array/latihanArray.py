import numpy as np

listNama = np.array([], dtype=object)       # pastikan array bisa menampung object/string


for i in range(4):
    nama = input("Masukkan nama: ")

    listNama = np.insert(listNama, 0, nama)

for i in range(len(listNama)-1,-1, -1):
    print(listNama[i])