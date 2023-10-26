sayi=int(input("Lütfen bir sayi giriniz"))
palindrom=str(sayi)[::-1]

if str(sayi) == palindrom :
    print("Sayi palindromdur")
else:
    print("Sayi palindrom değildir.")