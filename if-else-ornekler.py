#1-Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.Ehliyet almma koşulu en az 18 ve eğitim durumu liste ya da üniversite olmalıdır.

#isim = input("İsminizi giriniz: ")
#yas = int(input("Yaşınızı giriniz: "))
#egitim = input("Eğitim durumunuzu giriniz: ")

# if(yas>=18):
#     if(egitim=="lise" or egitim=="üniversite"):
#         print(f"{isim} ehliyet alabilirsin.")
#     else:
#         print(f"{isim} ehliyet alamazsın eğitim durumun yetersiz.")
# else:
#     print(f"{isim} ehliyet alamazsın yaşın tutmuyor")


# 2- Bir ögrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.

# yazili1 = int(input("1. yazılı notunuzu girin: "))
# yazili2 = int(input("2.yazılı notunuzu girin: "))
# sozlu = int(input("Sözlü notunuzu girin: "))

# ortalama = ((yazili1 + yazili2 + sozlu)/3)

# if (ortalama <24):
#     print("Notunuz 0")
# elif( 24>ortalama< 44):
#     print("Notunuz 1")
# elif(44<ortalama>55):
#     print("Notunuz 2")
# elif(54<ortalama>70):
#     print("Notunuz 3")
# elif(69<ortalama>85):
#     print("Notunuz 4")
# elif(84<ortalama>101):
#     print("Notunuz 5")        

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki biliglere göre hesaplanız.

# import datetime

# tarih = input("Aracınız hangi tarihte trafiğe çıktı (2025/4/5): ")
# tarih = tarih.split("/")
# trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCikis
# days = fark.days

# if days<=365:
#     print("1.servis aralığı")
# elif days>365 and days<=365*2:
#     print("2.serbis aralığı")
# elif days>365*2 and days <=365*3:
#     print("3.servis aralığı")
# else:
#     print("Hatalı süre")          
# 4- Kullanıcıdan bir sayı alıp, bu sayının pozitif, negatif veya sıfır olup olmadığını kontrol eden bir program yazınız.


    


