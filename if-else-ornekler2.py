'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi= float(input("sayı: ))

if (sayi >0) and (sayi<=100):
    print("sayı 0-100 arasında")
else:
    print("sayı 0-100 arasında değildir.)       



2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("sayı: "))
if (sayi > 0) :
    if(sayi % 2 ==0 ):
        print("Girilen sayı pozitif çift sayıdır.")
    else:
        print("Girilen sayı pozitif tek sayıdır.") 
else:
    print("Girilen sayı negatiftir.")


3- Email ve parola bilgileri ile giriş kontrolü yapınız        

email = "email@sadikturan.com"
password = "abc123"

girilenEmail = input("email: ")
girilenPassword = input("password: ")

if(girilenEmail == email):
    if(girilenPassword == password):
        print("Uygulamaya giriş başarılı")
    else:
        print("Şifre yanlış")
else:
    print("Email yanlış")    

    
    4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

    a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a>b) and (a>c):
    print("A en büyük sayıdır.")
elif(b>a) and (b>c):
    print("b en büyük sayıdır.")
elif(c>a) and (c>b):
    print("C en büyük sayıdır.")    


    5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
        Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
        a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
        b-)Finalden 70 alındıpında ortalamanın bir önemi olmasın.

        vize1 = float(input("Vize 1: "))
vize2 = float(input("Vize 2: "))
final1 = float(input("final: "))

ortalama = ((vize1+vize2)/2)*0.6 + (final1*0.4)

if(ortalama>=50):
    if(final1>=50):
        print(f"Ortalamanız: {ortalama} dersi geçtiniz. ")
    else:
        print(f"Ortalamanız: {ortalama} final notunuz 50'den az olduğu için dersi geçemediniz.")
else:
    print(f"Ortalamanız: {ortalama} ortalamanız 50'den aşağı olduğu için dersi geçemediniz.")

if (ortalama >=50):
    print(f"Ortalamanız: {ortalama} dersi geçtiniz.")
else:
    if(final1>=70):
        print(f"Ortalamanız: {ortalama} finalden 70 üzeri not aldığınız için dersi geçtiniz")
    else:
        print(f"Ortalamanız: {ortalama} dersi geçemediniz.")    


          
'''





     






       



  



