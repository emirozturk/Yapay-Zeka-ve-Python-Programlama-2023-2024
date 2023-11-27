"""
BMI hesabı yapan program
Ekrandan -1 girilene kadar alınan tüm değerlerin toplamını ekrana gösteren program
Girilen bir string’in içerisinde verilen bir karakterden kaç tane olduğunu bulan uygulamayı yazınız.
Rastgele n adet sayı tutup ekrana gösteren uygulama
Rastgele 1-10 arası n adet sayı tutup hangi sayıdan kaç adet geçtiğini gösteren uygulama
Girilen ad soyad ve yaş bilgilerine göre oluşturulan bir liste içerisinden rastgele 5 kişi seçilecektir. Seçilen kişinin 18 yaşından küçük olması durumunda bu 5 kişi içerisine dahil edilmeyecektir ve çekiliş işlemi tekrarlanacaktır.

"""
"""
Ekrandan girilen x değerinin y değerine göre bölümünden kalanı ekrana gösteren uygulama
x = int(input("X degeri"))
y = int(input("Y degeri"))
x2 = x
while x2>=y:
    x2 -= y
print(x2)
print(x % y)
"""
"""
Girilen 10 adet sayının en büyüğünü ve en küçüğünü bulan program
enKucuk = 2093489234923840923804982309489239048
enBuyuk = -293480923840923048092384092380948203
for _ in range(10):
    sayi = int(input("Sayi giriniz:"))
    if sayi<enKucuk:
        enKucuk = sayi
        print("Artık en küçük",sayi)
    if sayi>enBuyuk:
        enBuyuk = sayi
        print("Artık en büyük",sayi)

print(enKucuk,enBuyuk)

enKucuk = 2093489234923840923804982309489239048
enBuyuk = -293480923840923048092384092380948203
liste = []
for _ in range(10):
    sayi = int(input("Sayi giriniz:"))pyt
    liste.append(sayi)
print(liste)
liste.sort()
print(liste[0],liste[-1])
"""
"""
Rastgele n adet birbirinden farklı sayı tutup ekrana gösteren uygulama

import random

n = int(input("Kaç adet rastgele sayı tutulacak:"))
liste = []
while len(liste)<n:
    rastgele = random.randint(0,15)
    if rastgele not in liste:
        liste.append(rastgele)
print(liste)

import random

n = int(input("Kaç adet rastgele sayı tutulacak:"))
liste = list(range(15))
print(liste)
random.shuffle(liste)
print(liste[:n])
"""
"""
Piramidin tabanında kare biçiminde yerleştirilmiş N*N adet, ikinci katında (N-1)*(N-1), üçüncü katında (N-2)*(N-2), ... , N. katında (son kat) 1 taş blok olduğu kabul edilirse, piramitin kaç taş bloktan oluştuğunu ve kaç katlı olduğunu bulan programı yazınız (2.3 milyondan büyük olacak şekilde en az kaç kat olmalıdır).
Piramidin tam 24 yılda bittiğini ve işçilerin günde 10 saat çalıştıklarını düşünelim. İşçilerin bir saatte ortalama kaç blok yerleştirdiklerini bulan SaatBasinaBlok fonksiyonu yazınız (1 yıl = 365 gün + 6 saat kabul edilecek).

kat = 0
toplam = 0
while toplam <2_300_000:
    toplam += kat * kat
    print(f"Kat:{kat}, toplam:{toplam}")
    kat += 1

#Gün sayısı = 24*365 + 6
#Saat sayısı =(24*365 + 6)*10
print("Saatte ortalama blok sayısı:",toplam/((24*365 + 6)*10))

"""
"""
Parametre olarak aldığı sayıyı yazı olarak yazdıran fonksiyon

birler = ["Sıfır","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Atmış","Yetmiş","Seksen","Doksan"]

anaSayi = input("Sayi giriniz:")
sayi = anaSayi


if int(anaSayi)>10**4:
    deger = int(sayi[0])
    if deger!=0 and deger!=1:
        print(onlar[deger],end= " ")
    sayi = sayi[1:]

if int(anaSayi)>10**3:
    deger = int(sayi[0])
    if deger!=0 and deger!=1:
        print(birler[deger],end= " ")
    print("Bin",end=" ")
    sayi = sayi[1:]

if int(anaSayi)>10**2:
    deger = int(sayi[0])
    if deger!=0 and deger!=1:
        print(birler[deger],end= " ")
    print("Yüz",end=" ")
    sayi = sayi[1:]

if int(anaSayi)>10**1:
    deger = int(sayi[0])
    print(onlar[deger],end=" ")
    sayi = sayi[1:]

if int(anaSayi)>10**0:
    deger = int(sayi[0])
    if deger != 0:
        print(birler[deger])
    elif int(anaSayi)<10:
        print(birler[deger])
"""
"""
chat

siparisTutari = int(input("Sipariş tutarı:"))
kilogram = int(input("Kilogram"))
if siparisTutari<=100:
    siparisTutari+=kilogram
if siparisTutari>=200:
    siparisTutari*=.9
print("Sipariş tutarı:",siparisTutari)

"""

