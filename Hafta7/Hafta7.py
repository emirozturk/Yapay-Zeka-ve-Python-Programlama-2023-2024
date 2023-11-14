"""
liste = [1,2,3,4,5,6,6,4,3,3,5,7,8,9,0]
toplam = 0
for eleman in liste:
    toplam += eleman
ortalama = toplam / 15
print(ortalama)

liste = [1,2,3,4,5]
toplam = 0
for eleman in liste:
    toplam += eleman
ortalama = toplam / 5
print(ortalama)

liste = [1,2,3,4,5,4,4,4,44,4,6,6,6,6]
toplam = 0
for eleman in liste:
    toplam += eleman
ortalama = toplam / 14
print(ortalama)

def ortalamaHesapla(liste):
    toplam = 0
    for eleman in liste:
        toplam += eleman
    ortalama = toplam / len(liste)
    return ortalama

listeler =[[1,2,3,4,5,6,6,4,3,3,5,7,8,9,0],
           [1,2,3,4,5],
           [1,2,3,4,5,4,4,4,44,4,6,6,6,6]]
for liste in listeler:
    print(ortalamaHesapla(liste))
#n!/(n-r)!
#n!/((n-r)!*r!)
def fakt(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc*=i
    return sonuc

def perm(n,r):
    return fakt(n)/fakt(n-r)

def komb(n,r):
    return perm(n,r)/fakt(r)

n=5 
r=2
print("Permutasyon",perm(n,r))
print("Kombinasyon",komb(n,r))
import Islemler

print(Islemler.perm(5,3))
print(Islemler.asalAraligi(100,1000))
from Islemler import perm, asalMi
print(perm(5,3))
print(asalMi(123))
a = 1

def fonk():
    global a
    a = 5
    print(a)
    if 3<5:
        a = 3
        print(a)
fonk()
print(a)
"""


"""
fakt(5)
    5*fakt(4)
        4*fakt(3)
            3*fakt(2)
                2*fakt(1)
                    1*fakt(0)
                        1
"""
def fakt(n):
    if n == 0 or n == 1:
        return 1
    return n*fakt(n-1)

print(fakt(5))

def fib(n):
    if n == 0 or n==1: return 1
    return fib(n-1)+fib(n-2)