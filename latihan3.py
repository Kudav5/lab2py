# input nilai variabel
a = input("masukkan nilai a: ")
b = input("masukkan nilai b: ")

# cetak nilai variabel
print("Variabel a = ", a)
print("Variabel b = ", b)

# cetak hasil operasi kedua variabel dengan String Format
print("Hasil penggabungan", a, '&', b, '=', "{0}{1}".format(a,b))

# konversi nilai variabel
a = int(a)
b = int(b)
print("hasil penjumlahan", a,'+',b,"= %d" %(a+b))
print("hasil pembagian", a,'/',b,"= %d" %(a/b))