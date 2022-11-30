#Diktörgen, Kare ve Üçgen Alan ve Çevre Hesaplamaları#
print("Diktörgen, Kare ve Üçgen Alan ve Çevre Hesaplamaları")
print("Dikdörtgen Alan ve Çevre Hesaplaması")
kisa=input("Kısa Kenarı Girin : ")
uzun=input("Uzun Kenarı Girin : ")
alan=int(kisa)*int(uzun)
cevre=2*int(kisa)+2*int(uzun)
print("Dikdörtgenin Alanı : ",alan)
print("Dikdörtgenin Çevresi : ",cevre)
print("Kare Alan ve Çevre Hesaplaması")
kenar=input("Kenarı Girin : ")
alan=int(kenar)*int(kenar)
cevre=4*int(kenar)
print("Karenin Alanı : ",alan)
print("Karenin Çevresi : ",cevre)
print("Üçgen Alan ve Çevre Hesaplaması")
kenar=input("Kenarı Girin : ")
h=input("Yükseklik Girin : ")
alan=int(kenar)*int(h)/2
cevre=int(kenar)*3
print("Üçgenin Alanı : ",alan)
print("Üçgenin Çevresi : ",cevre)

#4 İşlem Hesaplamaları#
print("4 İşlem Hesaplamaları")
print("Toplama İşlemi")
a=input("1. Sayıyı Girin : ")
b=input("2. Sayıyı Girin : ")
sonuc=int(a)+int(b)
print("Sonuç : ",sonuc)
print("Çıkarma İşlemi")
a=input("1. Sayıyı Girin : ")
b=input("2. Sayıyı Girin : ")
sonuc=int(a)-int(b)
print("Sonuç : ",sonuc)
print("Çarpma İşlemi")
a=input("1. Sayıyı Girin : ")
b=input("2. Sayıyı Girin : ")
sonuc=int(a)*int(b)
print("Sonuç : ",sonuc)
print("Bölme İşlemi")
a=input("1. Sayıyı Girin : ")
b=input("2. Sayıyı Girin : ")
sonuc=int(a)/int(b)
print("Sonuç : ",sonuc)

#Değişken Olarak İsim Yazma#
print("Değişken Olarak İsim Yazma")
ad=input("Adınızı Girin : ")
soyad=input("Soyadınızı Girin : ")
kimlik=input("Kimlik Numaranızı Girin (Zorunlu Değil) : ")
sinif=input("Sınıf Şubenizi Girin : ")
okulno=input("Okul Numaranızı Girin : ")
telno=input("Telefon Numaranızı Girin (Zorunlu Değil) : ")
print("Ad : ",ad,"Soyad : ",soyad,"Kimlik : ",kimlik,"Sınıf : ",sinif,"Okul Numarası : ",okulno,"Telefon Numarası : ",telno)

okul_turu="meslek lisesi"
print(type(okul_turu))

a="Merhaba"
b="Canimmm"
c=a+b
print(c)

print("TR"*5)

a="Python"
b=a*10
print(b)

a="Hello World!"
bosluk=" "
b=a+bosluk
c=b*3
print(c)
