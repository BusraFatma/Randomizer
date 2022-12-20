import random
import time

print("Merhabalar: Değer giriniz.")
time.sleep(1)
print("Değer girmeniz bitince 'bitti' yazın")
time.sleep(1)
bitti = "bitti"
bitir = "bitir"
sonuç = "sonuç"
durum = ""
list = []
i = -1
while durum != bitti and durum != bitir and durum != sonuç:


    durum = input("Girin:")
    if durum != bitti and durum != bitir and durum != sonuç and durum != "göster":
        list.append(durum)
        i += 1
    elif durum == "göster":
        print(list)


uzunluk = len(list)


girdi = input("Yapılacak işlemi yaz: sadece bir tanesini istiyorsanız 1, sıralama istiyorsanız 2'ye basın:")
if girdi == "1":
    print(list[random.randint(0, uzunluk)])
elif girdi == "2":
    while uzunluk != 0:
        anan = random.randint(0, uzunluk-1)
        print(list[anan])
        list.pop(anan)
        uzunluk -= 1
bekleamk = input("bitirmek için tıklayın")





