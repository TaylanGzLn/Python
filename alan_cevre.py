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