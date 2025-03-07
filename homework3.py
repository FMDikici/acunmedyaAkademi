import os

def dosyaya_yaz(dosya_yolu, veri):
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        dosya.write(veri)

def dosyadan_oku(dosya_yolu):
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            print("\nDosya İçeriği:")
            print(icerik)
    else:
        print("Hata: Dosya bulunamadı!")

def coklu_satir_yaz(dosya_yolu):
    print("Lütfen 5 satır veri giriniz:")
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        for i in range(5):
            satir = input(f"Satır {i+1}: ")
            dosya.write(satir + "\n")

def satirlari_oku(dosya_yolu):
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            print("\nDosyadan Okunan Satırlar:")
            for satir in dosya:
                print(satir.strip())
    else:
        print("Hata: Dosya bulunamadı!")

def main():
    dosya_yolu = "cikti.txt"
    tek_girdi = input("Bir metin girin: ")
    dosyaya_yaz(dosya_yolu, tek_girdi)
    dosyadan_oku(dosya_yolu)
    
    coklu_dosya_yolu = "coklu_satirlar.txt"
    coklu_satir_yaz(coklu_dosya_yolu)
    satirlari_oku(coklu_dosya_yolu)

if __name__ == "__main__":
    main()