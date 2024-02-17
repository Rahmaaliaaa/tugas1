import datetime

tanggal = int(input("Masukan Tanggal lahir: "))
bulan = int(input("Masukan bulan lahir: "))
tahun = int(input("Masukan tahun  lahir: "))

sekarang = datetime.date.today()
lahir = datetime.date(tahun, bulan, tanggal)
umur = sekarang - lahir
tahun = umur.days // 365
bulan = (umur.days % 365) // 30
hari = (umur.days % 365) // 30

print(f"umur: {tahun} Tahun, {bulan} Bulan, {hari} Hari")