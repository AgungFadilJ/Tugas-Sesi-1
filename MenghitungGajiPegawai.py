GajiPokok = int(input("Gaji Pegawai : "))
Perhari = int(input("Kerja Berapa Hari : "))

UangTransport = 100000 * Perhari
UangMakan = 50000 * Perhari

JamLembur = int(input("Berapa Jam Lembur : "))

if JamLembur <= 2:
    UpahLembur = JamLembur *Perhari
else:
    UpahLembur = 200000 + (JamLembur - 2) *150000
    
Honor = GajiPokok + UangTransport + UangMakan + UpahLembur

print("Honor Yang Diterima : ", Honor , " Rupiah ")