

    
nama = (input("Nama Anda :"))
bulan = int (input("Berapa lama anda bekerja [bulan] :"))

if bulan >= 48:
    print(nama, "Anda adalah pegawai tetap")
    print("Gaji : Rp 6.000.000")
    print("Tunjangan : \n - BPJS kelas I, \n - keluarga, \n - Hari Raya")

elif bulan >= 36 :
    print (nama, "Anda Bukan Pegawai Tetap")
    print ("Gaji : Rp 5.000.000")
    print ("Tunjangan : \n - BPJS kelas II, \n - Keluarga")
elif bulan >=12:
    print(nama, "Anda Bukan Pegawai Tetap")
    print("Gaji : Rp 4.000.000")
    print("Tunjungan : -")
elif bulan < 12:
    print(nama, "Anda Bukan Pegawai Tetap")
    print("Gaji : Rp 3.000.000")
    print("Tunjangan : -")

