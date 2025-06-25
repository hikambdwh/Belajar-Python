#LATIHAN IF ELSE STATEMENT
import math as mtk

print(20*"=")
print("KALKULATOR")
print(20*"=")

x = int(input("angka pertama: "))
y = int(input("angka kedua  : "))
operasi = input("operasi  : ")

if operasi == "x":
	hasil = x * y
	print(f"{x} x {y} = {hasil}")

elif operasi == "+":
	hasil = x + y;
	print(f"{x} + {y} = hasil")

elif operasi == "-":
	hasil = x - y
	print(f"{x} - {y} = {hasil}")

elif operasi == "/":
	if y != 0:
		hasil = x / y
		print(f"{x} / {y} = {hasil:.2f}")

	else:
		print("angka kedua harus lebih dari 0")

else:
	print("goblok anda") 


print(f"hasil dari akar 144 adalah {mtk.sqrt(144):.0f} dan phi bernilai {mtk.pi:.2f}")
