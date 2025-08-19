'''Membuat fungsi'''

def hello_world():
    '''fungsi menampilkan hello world'''
    print("hello world")
    print("Kepada Ucup Surucup")
    print("Dan juga kepada Otong Surotong")

hello_world()
hello_world()

# fungsi()

def fungsi():
    '''pemanggilan fungsi harus setelah dibuat'''
    print("Ini adalah fungsi")

fungsi()

def matematika(sisi, tinggi):
    hasil = (sisi * tinggi) / 2

    return hasil


sisi = int(input("sisi:"))
tinggi = int(input("tinggi:"))
print(f"{matematika(sisi,tinggi):.0f}")