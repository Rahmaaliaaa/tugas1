indeks ={
    "Reamur     " : "r",
    "Celcius    " : "c",
    "Fahrenheit " : "f",
    "Kelvin     " : "k"
}
print("==========Indeks Satuan Skala Suhu==========")
for i in indeks :
    print("Satuan suhu :", i , "\t Indeks : ",indeks[i])

suhu = float(input("Masukan Suhu : "))
satuan = input("Masukan indeks skala suhu : ") 

if (satuan == "r"):
    print(suhu, "derajat reamur : ")
    print("Celcius =", (suhu*5/4), "derajat")
    print("Fahrenheit =", (suhu*9/4)+32, "derajat")
    print("Kelvin =", (suhu*5/4)+ 273, "derajat")