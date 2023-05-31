import os

class Musteri():
    def __init__(self,TC,SIFRE,ISIM):
        self.tc = TC
        self.sifre = SIFRE
        self.isim = ISIM
        self.bakiye = 0


class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,TC,SIFRE,ISIM):
        self.musteriler.append(Musteri(TC,SIFRE,ISIM))
        print("Kayıt Olduğunuz İçin Teşekkür Ederiz")


banka = Banka()

while True:
    os.system("cls")
    print("""
      1-Müsteriyim
      2-Müşteri Olmak İstiyorum      
    
    """)

    secim = int(input("Seçiminiz : "))

    if secim== 1:
        tcx = [a.tc for a in banka.musteriler]
        TC = input("TC : ")
        if TC in tcx:
            for musteri in banka.musteriler:
                if TC == musteri.tc:
                    sifre = input("Lütfen Şifrenizi Giriniz : ")
                    if sifre == musteri.sifre:
                        print("Hoş Geldiniz Sayın {}".format(musteri.isim))
                        while True:
                            os.system("cls")
                            print("""                                      
                                    1-Bakiye Sorgula
                                    2-Hesabına Para Yatır
                                    3-Para Gönder
                                    4-Para Çek
                                    Q-Çıkış    
                        
                                     """)
                            secim2 = input("İşlem Numarınızı Seçiniz : ")

                            if secim2 == "1":
                                print("Bakiyeniz : {}".format(musteri.bakiye))
                                input("Ana Menüye dönmek için enter'a basınız")
                            elif secim2 == "2":
                                miktar = int(input("Miktar : "))
                                onay = input(
                                    "Kendi hesabınıza {} TL para Yatırmayı onaylıyor musunuz?  E/H\n".format(miktar))
                                if onay == "E" or onay == "e":
                                    musteri.bakiye += miktar
                                    print("Paranız Yatırıldı")
                                    input("Ana Menüye Dönmek için entera basınız")
                                elif onay == "H" or onay == "h:":
                                    print("İşleminiz İptal Edildi")
                                    input("Ana Menüye Dönmek için enter'a basınız")

                                else:
                                    print("Hatalı giriş yaptınız, İşlem iptal edildi")
                                    input("Ana menüye dönmek için enter'a basınız")
                            elif secim2 == "3":
                                arananTC = input("Müşteri TC : ")
                                if arananTC in tcx:
                                    for digerMusteri in banka.musteriler:

                                        if arananTC == digerMusteri.tc:

                                            miktar = int(input("Miktar : "))
                                            if miktar <= musteri.bakiye:

                                                onay = input(
                                                    "{} adlı müsterimize {} TL tutarında para yatırmayı kabul ediyor musunuz? E/H\n.".format(digerMusteri.isim,miktar))

                                                if onay == "e" or onay == "E":
                                                    digerMusteri.bakiye += miktar
                                                    musteri.bakiye -= miktar
                                                    print("Para aktarıldı")
                                                    input("Ana Menüye dönmek için enter'a basınız")

                                                elif onay =="h" or onay =="H":
                                                    print("İşlem iptal edildi")
                                                    input("Ana Menüye dönmek için enter'a basınız")
                                                else:
                                                    print("Hatalı giriş,İşlem iptal oldu.")
                                                    print("Ana Menüye dönmek için enter'a basınız")

                                            else:
                                                print("Bakiyeniz Yetersiz")
                                                input("Ana menüye dönmek için enter'a basınız!")

                                    else:
                                            print("Müşteri Bulunamadı!")

                            elif secim2 == "4":
                                miktar = int(input("Miktar: "))
                                if miktar <= musteri.bakiye:
                                    musteri.bakiye -= miktar
                                    print("İşlem tamamlandı,paranızı alın!")
                                    input("Ana Menüye dönmek için enter'a basınız")

                                else:
                                    print("Bakiyeniz yetersiz")
                                    input("Ana Menüye dönmek için enter'a basınız")
                            elif secim2 == "q" or secim2== "Q":
                                break


    elif secim ==2:
        a = input("TC Giriniz : ")
        b = input("İsim Giriniz : ")
        c = input("Şifre Giriniz : ")
        banka.musteri_ol(a,c,b)
        input("Ana Menüye dönmek için enter'a basınız")


    else:
        print("Hatalı seçim yaptınız!")


else :
    























