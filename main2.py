faiz=1.59
vade ="36"
krediAdi="İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)

faiz=str(faiz)
print=type(faiz)

vade=int(input("Lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
vade=vade+12

print("Seçtiğiniz vade sonucunu ortaya çıkan vade:"+str(vade))
print("Seçtiğiniz vade sonucunu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

metin=f"Hosgeldiniz {1+1}"

#listeler

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","konut Kredisi"]
print(type(krediler))

krediler.append("Özel Kredi")
print(krediler[3])

krediler.pop(0)

print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z Kredisi"])
print(krediler)

#for

for i in range(10):
    print("xx")
    print(i)
print("*********")
for i in range(5,10):
    print(i)
print("*********")
krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]

for kredi in krediler:
    print(kredi)


#sonsuz döngü
i=0
while i<10:
    print("x")
    i+=1
print("y")

while i<len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i]=="Konnut Kredisi":
        break

#fonksiyonlar

fiyat=100
indirim=20

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba{name}")


calculate()
calculateWithParams(50,10)
sayHello("Fatih")

def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat=calculateAndReturn(200,50)

print(yeniFiyat)