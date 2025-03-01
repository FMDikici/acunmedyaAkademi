def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == '-':
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == '*':
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"

# Örnek Kullanım
print(hesap_makinesi(5, 3, '+'))  # Çıktı: 5 + 3 = 8
print(hesap_makinesi(10, 2, '/')) # Çıktı: 10 / 2 = 5.0
print(hesap_makinesi(4, 0, '/'))  # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
print(hesap_makinesi(6, 2, '%'))  # Çıktı: Geçersiz işlem türü!
