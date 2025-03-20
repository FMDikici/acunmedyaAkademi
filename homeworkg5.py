def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    if sayi2 != 0:
        bolum = sayi1 / sayi2
    else:
        bolum = "Bölme işlemi sıfıra yapılamaz."
    
    return toplam, fark, carpim, bolum

def palindrom_mu(kelime):
    if kelime == kelime[::-1]:
        return f"{kelime} -> palindrom"
    else:
        return f"{kelime} -> değil"

def yasta_100e_ulasma(yas):
    yil_sonra = 100 - yas
    return yil_sonra

# Kullanıcıdan girişler alalım
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
kelime = input("Bir kelime girin: ")
yas = int(input("Yaşınızı girin: "))

# Fonksiyonları çağırıp sonuçları yazdıralım
toplam, fark, carpim, bolum = hesap_makinesi(sayi1, sayi2)
print(f"\nHesap Makinesi Sonuçları:")
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")

print(f"\nPalindrom Kontrol Sonucu: {palindrom_mu(kelime)}")

print(f"\n100 yaşına {yasta_100e_ulasma(yas)} yıl sonra ulaşacaksınız.")
