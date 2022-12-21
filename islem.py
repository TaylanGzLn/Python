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