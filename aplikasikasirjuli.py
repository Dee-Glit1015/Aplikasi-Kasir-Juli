# Aplikasi Kasir

# def main ():

import sys 
total = []

print ("-------------")
print ("Kasir Desy")
print ("-------------")
# pilih = int(input("Masukkan Pilihan Anda :"))
# import random
# comp = random.randint(1,3)

def daftar_barang ():
    print("No | Nama Barang | Harga")
    print("1 | Downy | 23.000")
    print("2 | Baygon | 41.100")
    print("3 | Mamy Poko | 59.000")
    print("4 | Ovaltine | 23.000")
    print("5 | Beras | 70.000")
    print ("-------------------")
    kode = int (input("Masukan Jumlah Barang :"))
    # import random
    # comp = random.randint(1,5)
    if kode == 1 :
        #  if comp == 1:
        jumlah1 = int (input("Masukan Jumlah Barang"))
        total1 = 23.000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        # elif comp == 2:
        jumlah2 = int(input ("Masukan Jumlah Barang :"))
        total2 = 41.000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        # elif comp == 3:
        jumlah3 = int (input("Masukan Jumlah Barang :"))
        total3 = 59.000 * jumlah3
        total.append (total3)
        tanya()
    elif kode == 4:
        # elif comp == 4:
        jumlah4 = int (input("Masukan Jumlah Barang :"))
        total4 = 23.000* jumlah4
        total.append (total4)
    elif kode == 5:
        # elif comp == 5:
        jumlah5 = int (input("Masukan Jumlah Barang :"))
        total5 = 70.000 * jumlah5
        total.append (total5)
        tanya ()
    return

def tanya () :
    print("\n----------------")
    tanya = input("Ingin tambah barang ? [y/n]:")
    if tanya == "y" :
        daftar_barang()
    elif tanya == "n" :
        akhir ()
    else :
        print("Pilihan Yang Anda Masukan Salah !")

def akhir () :
    for harga in total :
        print ("Subtotal :", sum (total))
        diskon = 0
        a = sum (total)
        if a > 500.000:
            diskon = a*8 /100
        elif a > 300.000:
            diskon = a*5 /100
        elif a> 200.000 :
            diskon = a*3 /100
        elif a > 100.000:
            diskon = a * 1/100
        else :
            diskon=0

        print(" Potongan Harga :", diskon)
        totalakhir = a - diskon
        print("Total :", totalakhir)
        print("--------------------")
        bayar =int (input("Bayar :"))
        kembalian = bayar - totalakhir
        print("Kembalian :", kembalian)
        print("-----------------")
        print("Terima Kasih")
        print("----------------")

daftar_barang()
