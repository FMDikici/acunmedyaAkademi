for i in range(1, 101):
    print(i, end=" ")
print()

for i in range(2, 101, 2):
    print(i, end=" ")
print()

sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")

print("1'den 100'e kadar olan asal sayılar:")
for num in range(2, 101):
    asal = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            asal = False
            break
    if asal:
        print(num, end=" ")
print()