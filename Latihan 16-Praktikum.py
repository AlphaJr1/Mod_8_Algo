def pangkat(pkt = 0,akt = 0):
    if (akt == 0):
        return 0
    else:
        pkt = int(input("Masukkan pangkatnya : "))
        return akt**pkt


angka = int(input("Masukkan angka : "))
hasil = pangkat(akt = angka)
print("Hasil pangkatnya adalah :"+ str(hasil))



