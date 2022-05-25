class project:
   def __init__(self, sahibi, konusu, teslim, yazilandil):
     self.sahibi = sahibi
     self.konusu = konusu
     self.teslim = teslim
     self.yazilandil = yazilandil

project_1 = project("Proje sahibi: Emirhan GEÇER", "Proje konusu: Modlu Taş Kağıt Makas oyunu", "Proje teslim tarihi: 20.05.2022" ,"Projenin yazıldığı dil: Python" )

print(project_1.sahibi)
print(project_1.konusu)
print(project_1.teslim)
print(project_1.yazilandil)


import sqlite3
with sqlite3.connect('taskagıtmakasson.db') as baglanti:

    imlec = baglanti.cursor()
    imlec.execute("SELECT * from karakterler")
    baglanti.commit()
print("kullanılan karakterlerimiz:", imlec.fetchall())
import random
secenek=["kalem","taş","kağıt","makas","kertenkele","spock"]
taş=secenek[1]
kağıt=secenek[2]
makas=secenek[3]
kalem=secenek[0]
kertenkele=secenek[4]
spock=secenek[5]
startrek={"KERTENKELE":"Zehirlidir dikkat",
         "SPOCK":"star trekteki düz siyah saçlı bir abimiz"}
sozlukkalem={"Kalem":"kırılgan diyorlar aslında ama incinmişsin diyen de var karakterimize"}

def menu():
    print("ana menüye dönülüyor...")

print("\n****** Modlu Taş,Kağıt,Makas oyununa hoş geldiniz ******\n")


while True:
    modsecim = int(input(
        "\nAşağıdaki oyun modlarından birini seçiniz\n\n Klasik oyun modu için 1'i tuşlayınız\n Kalem+ oyun modu için 2'yi tuşlayınız\n STAR TREK modu için 3'ü tuşlayınız\n Çıkmak için 0'ı tuşlayınız\ndiğer modlar için beklemede kalınız. Çok yakında...\n"))

    if modsecim == 1:
        print("****** Klasik oyun modumuza hoş geldiniz. Oyunu bitirmek ve ana menüye dönmek için q harfini tuşlayınız, iyi oyunlar:) ******")
        while True:
            secim = input("Taş mı kağıt mı makas mı?")
            bil_secim = random.choice(secenek[1:4])
            if secim == 'q':
                print(menu())
                break
            if secim==taş:
                if bil_secim==taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Berabere")
                elif bil_secim==kağıt:
                    print("Bilgisayarın seçimi: Kağıt Kaybettiniz")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç:Kazandınız")
            if secim==kağıt:
                if bil_secim==taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
                elif bil_secim==kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç:Kaybettiniz")
            if secim==makas:
                if bil_secim==taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
                elif bil_secim==kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç:Berabere")


    elif modsecim == 2 :

        print("****** Kalem+ oyun modumuza hoş geldiniz. Oyunu bitirmek ve ana menüye dönmek için q harfini tuşlayınız, iyi oyunlar:) ******\n")
        print("Bu modda bulunan karakterimizi tanıyalım.\n")
        print(sozlukkalem.items())
        while True:
            secim = input("\nTaş mı kağıt mı makas mı kalem mi? ")
            bil_secim = random.choice(secenek[0:4])
            if secim == 'q':
                print(menu())
                break

            if secim == taş:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Berabere")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kaybettiniz")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç: Kazandınız")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç:Kazandınız")
            if secim == kağıt:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç: Kaybettiniz")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç:Kaybettiniz")
            if secim == makas:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç: Kazandınız")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç:Berabere")
            if secim == kalem:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç : Berabere")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç: Kaybettiniz")
    elif modsecim == 3 :

        print("****** STAR TREK oyun modumuza hoş geldiniz. Oyunu bitirmek ve ana menüye dönmek için q harfini tuşlayınız, iyi oyunlar:) ******\n")
        print("Öncesinde yeni karakterlerimizi tanıyalım\n")
        print(startrek.items())
        while True:
            secim = input("\nTaş mı kağıt mı makas mı? YA DAA KERTENKELE Mİİİ SPOCK MUUU????")
            bil_secim = random.choice(secenek[1:6])
            if secim == 'q':
                print(menu())
                break

            if secim == taş:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Berabere")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kaybettiniz")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç: Kazandınız")
                elif bil_secim == kertenkele:
                    print("Bilgisayarın seçimi: kertenkele Sonuç: Kazandınız")
                else:
                    print("Bilgisayarın seçimi: spock Sonuç: Kaybettiniz")

            if secim == kağıt:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç: Kaybettiniz")
                elif bil_secim == kertenkele:
                    print("Bilgisayarın seçimi: kertenkele Sonuç: Kaybettiniz")
                else:
                    print("Bilgisayarın seçimi: spock Sonuç: Kazandınız")

            if secim == makas:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
                elif bil_secim == kalem:
                    print("Bilgisayarın seçimi: Kalem Sonuç: Kazandınız")
                elif bil_secim == kertenkele:
                    print("Bilgisayarın seçimi: kertenkele Sonuç: Kazandınız")
                else:
                    print("Bilgisayarın seçimi: spock Sonuç: Kaybettiniz")

            if secim ==kertenkele:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
                elif bil_secim ==kertenkele:
                    print("Bilgisayarın seçimi: Kertenkele Sonuç : Berabere")
                elif bil_secim == spock:
                    print("Bilgisayarın seçimi: spock Sonuç: Kazandınız")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç: Kaybettiniz")

            if secim ==spock:
                if bil_secim == taş:
                    print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
                elif bil_secim == kağıt:
                    print("Bilgisayarın seçimi: Kağıt Sonuç: Kaybettiniz")
                elif bil_secim ==kertenkele:
                    print("Bilgisayarın seçimi: Kertenkele Sonuç : Kaybettiniz")
                elif bil_secim == spock:
                    print("Bilgisayarın seçimi: spock Sonuç: Berabere")
                else:
                    print("Bilgisayarın seçimi: makas Sonuç: Kazandınız")

    elif modsecim == 0:

            print("Çıkılıyor...")

            break

    else:

            print("yanlış bir tuşlama yaptınız")

            break

