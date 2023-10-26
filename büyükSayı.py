birinciSayi=int(input("Lütfen birinci sayiyi giriniz."))
ikinciSayi=int(input("Lütfen ikinci sayiyi giriniz."))
ücüncüSayi=int(input("Lütfen ücüncü sayiyi giriniz."))
    
if birinciSayi>ikinciSayi and birinciSayi>ücüncüSayi:
    print("En büyük sayi :", birinciSayi)

elif ikinciSayi>birinciSayi and ikinciSayi>ücüncüSayi:

    print("En büyük sayi :",ikinciSayi)

else:
    print("En büyük sayi :",ücüncüSayi)