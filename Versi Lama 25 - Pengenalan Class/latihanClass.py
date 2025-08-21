class murid():
    nama = "nama"

    def perkenalan(self, nim):
        print(f"""
            Nama: {self.nama}
            NIM:  {nim}
            """)


murid1 = murid()
murid2 = murid()

murid1.nama = "otong"
murid2.nama = "ucup"
murid1.perkenalan(2300798)
murid2.perkenalan(2300844)

