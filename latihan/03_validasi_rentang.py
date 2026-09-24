# Program: 03_validasi_rentang.py
# Deskripsi: Menerima sudut dalam derajat dan memvalidasi rentangnya (0 < sudut < 180).

sudut = float(input("Besar sudut dalam derajat: "))

if sudut <= 0 or sudut >= 180:
    print("Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
elif sudut < 90:
    print("Sudut lancip")
elif sudut == 90:
    print("Sudut siku-siku")
else:
    print("Sudut tumpur") # atau tumpul sesuai modul