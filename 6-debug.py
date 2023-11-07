liste1=list([x*10 for x in range(1,50,2)[:10]])
liste2=list(range(100,1000,8)[:10])
liste3=list(range(193,1000,7)[:10])
aranan = [105,108,250,235,135,185,176,156,233,189]
listeler = [liste1,liste2,liste3]
print(listeler)
farklar=[]
for liste in listeler:#Her liste için   
    fark = 0
    for i in range(10):#Elimdeki liste ile karşılaştır
        fark += abs(liste[i]-aranan[i])#Toplam farkı bul
    farklar.append(fark)
#minimum farka sahip olanın indisini bul
minFark = 10000000
minIndis = 0
for i in range(len(farklar)):
    if farklar[i] < minFark:
        minFark = farklar[i]
        minIndis = i
print("En yakın",minIndis,"indisindeki diziye benziyor")
