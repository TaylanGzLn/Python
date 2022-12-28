#Diğer Kodlamalar#
print("Diğer Kodlamalar")

okul="Lise"
print(type(okul))

#Değişken Olarak Metin Yazma#
print("Değişken Olarak Metin Yazma Komudu")
a="Hello"
b="World!"
c=a+b
print(c)

#Metni Tekrarlama#
print("Metni Tekrarlama Komudu")
print("Hello World!"*5)

#Değişken Olarak Metin Tekrarlama#
print("Değişken Olarak Metin Tekrarlama Komudu")
a="Hello World!"
b=a*10
print(b)

#Değişken Olarak Metin Yazma Ve Tekrarlama#
print("Değişken Olarak Metin Yazma Ve Tekrarlama Komudu")
a="Hello World!"
bosluk=" "
b=a+bosluk
c=b*3
print(c)

#Mesajı Tekrarlama#
print("Mesajı Tekrarlama Komudu")
for i in range(5):
  print("Hello World!")

#Listeleme Yöntemi#
print("Listeleme Yöntemi")

ilk_liste=["Ankara", 312, 0.6]
print(ilk_liste)

asal_sayilar=[2, 3, 5, 7, 11, 13, 17, 19, 23]
print(asal_sayilar[0:6:2])

tek_sayilar=[3, 5, 7, 9, 11, 13, 15, 17, 19]
print(tek_sayilar[0:6])
print(tek_sayilar[2:5])
print(tek_sayilar[3:8])
print(tek_sayilar[:5])
print(tek_sayilar[3:])
print(tek_sayilar[0:8:2])
print(tek_sayilar[::3])

sehirler=["Ankara", "Bursa", "Çanakkale", "Denizli", "Eskişehir"]
print(sehirler[2])

sehirler=["Ankara", "Bursa", "Çanakkale", "Denizli", "Eskişehir"]
print(sehirler[-2])

ders=['K','O','D','L','A','M','A']
print(ders[0])
print(ders[2])
print(ders[5])