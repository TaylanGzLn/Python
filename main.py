#Diktörgen, Kare, Üçgen ve Daire Alan ve Çevre Hesaplamaları#
print("Diktörgen, Kare, Üçgen ve Daire Alan ve Çevre Hesaplamaları")

#Dikdörtgen Alan ve Çevre Hesaplaması#
print("Dikdörtgen Alan ve Çevre Hesaplaması")
kisa=int(input("Kısa Kenarı Girin : "))
uzun=int(input("Uzun Kenarı Girin : "))
alan=kisa*uzun
cevre=2*kisa+2*uzun
print("Dikdörtgenin Alanı : ",alan)
print("Dikdörtgenin Çevresi : ",cevre)

#Kare Alan ve Çevre Hesaplaması#
print("Kare Alan ve Çevre Hesaplaması")
kenar=int(input("Kenarı Girin : "))
alan=kenar*kenar
cevre=4*kenar
print("Karenin Alanı : ",alan)
print("Karenin Çevresi : ",cevre)

#Üçgen Alan ve Çevre Hesaplaması#
print("Üçgen Alan ve Çevre Hesaplaması")
kenar=int(input("Kenarı Girin : "))
h=int(input("Yükseklik Girin : "))
alan=(kenar*h)/2
cevre=kenar*3
print("Üçgenin Alanı : ",alan)
print("Üçgenin Çevresi : ",cevre)

#Dairenin Yarıçapı İle Alan ve Çevre Hesaplaması#
print("Dairenin Yarıçapı İle Alan ve Çevre Hesaplaması")
r=float(input("Yarı Çapı Girin : "))
alan=3.14*r*r
cevre=2*3.14*r
print("Dairenin Alanı : ",alan)
print("Dairenin Çevresi : ",cevre)

#4 İşlem Hesaplamaları#
print("4 İşlem Hesaplamaları")
def toplama(a, b):
    return a+b
def cikarma(a, b):
    return a-b
def carpma(a, b):
    return a*b
def bolme(a, b):
    return a/b
print("Yapacağınız İşlemi Seçiniz. \n",
        "1. Toplama \n",
        "2. Çıkarma \n",
        "3. Çarpma \n",
        "4. Bölme"
)
secim=int(input("Şeçtiğiniz işlemi 1, 2, 3, 4 olacak şekilde giriniz : "))
a=int(input("1. Sayıyı Girin : "))
b=int(input("2. Sayıyı Girin : "))
if secim ==1:
    print(a, "+", b, "=", toplama(a, b))
if secim ==2:
    print(a, "-", b, "=", cikarma(a, b))
if secim ==3:
    print(a, "*", b, "=", carpma(a, b))
if secim ==4:
    print(a, "/", b, "=", bolme(a, b))

#Yaş Hesaplaması#
print("Yaş Hesaplaması")
ad=input("Adınızı Girin : ")
dogum=int(input("Doğum Yıl Tarihinizi Girin : "))
guncel=int(input("Güncel Yılı Giriniz : "))
yas=guncel-dogum
print("Merhaba",ad,"yaşınız",yas,"'dır")

#Değişken Olarak İsim Yazma#
print("Değişken Olarak İsim Yazma")
ad=input("Adınızı Girin : ")
soyad=input("Soyadınızı Girin : ")
kimlik=input("Kimlik Numaranızı Girin (Zorunlu Değil) : ")
sinif=input("Sınıf Şubenizi Girin : ")
okulno=input("Okul Numaranızı Girin : ")
telno=input("Telefon Numaranızı Girin (Zorunlu Değil) : ")
print("Ad : ",ad,"Soyad : ",soyad,"Kimlik : ",kimlik,"Sınıf : ",sinif,"Okul Numarası : ",okulno,"Telefon Numarası : ",telno)

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