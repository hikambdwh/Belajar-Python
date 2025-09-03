class kendaraan():
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    
class motor(kendaraan):
    def __init__(self, nama, warna, roda, merk ):
        super().__init__(nama, warna)
        self.roda = roda
        self.merk = merk

class mobil(kendaraan):
    def __init__(self, nama, warna, tahun, tipe):
        super().__init__(nama, warna)
        self.tahun = tahun
        self.tupe = tipe

def info(transportasi):
    print(f"""
        Nama: {transportasi.nama}
        warna: {transportasi.warna}         
        """)


motor1 = motor("motor", "merah", 2, "suzuki")
mobil1 = mobil("mobil", "hijau", 4, "toyota")
print(motor1.__dict__)
 
info(motor1)
info(mobil1)

