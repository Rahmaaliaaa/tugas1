import math

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def main():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    sisi1 = float(input("Masukkan panjang sisi pertama segitiga: "))
    sisi2 = float(input("Masukkan panjang sisi kedua segitiga: "))
    sisi3 = float(input("Masukkan panjang sisi ketiga segitiga: "))

    luas = hitung_luas_segitiga(alas, tinggi)
    keliling = hitung_keliling_segitiga(sisi1, sisi2, sisi3)

    print("Luas segitiga adalah:", luas)
    print("Keliling segitiga adalah:", keliling)

if __name__ == "__main__":
    main()
