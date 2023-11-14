def fakt(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc*=i
    return sonuc

def perm(n,r):
    return fakt(n)/fakt(n-r)

def komb(n,r):
    return perm(n,r)/fakt(r)

def asalMi(sayi):
    for i in range(2,sayi):
        if sayi % i == 0:
            return False
    return True

def asalAraligi(baslangic,bitis):
    liste = []
    for sayi in range(baslangic,bitis+1):
        if asalMi(sayi):
            liste.append(sayi)
    return liste
