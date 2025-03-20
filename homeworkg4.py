sayilar = []
for _ in range(5):
    sayi = float(input("Bir sayı girin: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")

kelimeler = []
kac_kelime = int(input("Kaç kelime gireceksiniz? "))
for _ in range(kac_kelime):
    kelime = input("Bir kelime girin: ")
    kelimeler.append(kelime)

kelimeler.reverse()
print("Ters sıralı kelimeler:", kelimeler)

liste = input("Liste elemanlarını boşlukla ayırarak girin: ").split()
tekrarsiz_liste = list(set(liste))
print("Tekrarsız liste:", tekrarsiz_liste)