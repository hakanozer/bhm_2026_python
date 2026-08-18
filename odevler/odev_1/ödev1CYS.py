# Soru 1

# Kullanıcının adını ve yaşını input() ile alınız. Daha sonra ekrana aşağıdaki formata benzer şekilde yazdırınız.

# Örnek Çıktı:
# Merhaba Ahmet, yaşınız 25.

name = input("Adınızı giriniz: ")
age = input("Yaşınızı giriniz: ")

print(f"Merhaba {name}, yaşınız {age}.")

# Soru 2

# İki adet sayıyı kullanıcıdan alınız. Sayıları int veri tipine dönüştürerek;

# Toplamını
# Farkını
# Çarpımını
# Bölümünü

# ekrana yazdırınız. Hatalı girişlerde try-except kullanarak kullanıcıya uyarı veriniz.

try:
    num1 = int(input("Birinci sayıyı giriniz: "))
    num2 = int(input("İkinci sayıyı giriniz: "))

    toplam = num1 + num2
    fark = num1 - num2
    carpim = num1 * num2
    bolum = num1 / num2

    print(f"Toplam: {toplam}")
    print(f"Fark: {fark}")
    print(f"Çarpım: {carpim}")
    print(f"Bölüm: {bolum}")
except : #burada zero division error ve value error beraber ele alınmıştır.
    print("Lütfen geçerli bir sayı giriniz.") 

# Soru 3

# Bir değişken içerisinde aşağıdaki metin bulunmaktadır.

# text = "Python Programlama Dili"

# Bu metin üzerinde;

# Tamamını büyük harfe çeviriniz.
# Tamamını küçük harfe çeviriniz.
# İlk harfleri büyük olacak şekilde yazdırınız.
# Karakter sayısını ekrana yazdırınız.
# "Programlama" kelimesini "Yazılım" ile değiştiriniz.

text = "Python Programlama Dili"
print(text.upper())
print(text.lower())
print(text.title())
print(len(text))
print(text.replace("Programlama", "Yazılım"))

# Soru 4

# Kullanıcıdan bir e-posta adresi alınız.

# Girilen e-posta adresinin başındaki ve sonundaki boşlukları temizleyiniz (strip()).

# Daha sonra adres içerisinde "@" karakteri olup olmadığını kontrol ederek sonucu ekrana yazdırınız.

email = input("E-posta adresinizi giriniz: ").strip()
if "@" not in email:
    print("Geçerli bir e-posta adresi giriniz.")
else:
    print("ok")

# Soru 5

# Kullanıcıdan kullanıcı adı ve şifre alınız.

# Aşağıdaki bilgiler ile karşılaştırınız.

# username = "admin"
# password = "12345"

# Her iki bilgi doğruysa "Giriş Başarılı", aksi durumda "Kullanıcı adı veya şifre hatalı." mesajını yazdırınız.

username = input("Kullanıcı adınızı giriniz: ")
password = input("Şifrenizi giriniz: ")
if username == "admin" and password == "12345":
    print("Giriş Başarılı")
else:
    print("Kullanıcı adı veya şifre hatalı.")

# Soru 6

# Kullanıcıdan bir yaş bilgisi alınız.

# Yaş 18 ve üzerindeyse "Ehliyet alabilirsiniz."
# Değilse "Ehliyet alamazsınız."

# mesajını ekrana yazdırınız.

age = int(input("Yaşınızı giriniz: "))
if age >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")

# Soru 7

# Kullanıcıdan bir not (0-100) alınız.

# Aşağıdaki tabloya göre harf notunu hesaplayınız.

# Puan	Harf Notu
# 90-100	AA
# 80-89	BA
# 70-79	BB
# 60-69	CB
# 50-59	CC
# 0-49	FF

# Sonucu ekrana yazdırınız.

grade = int(input("Notunuzu giriniz: "))
if 90 <= grade <= 100:
    print("AA")
elif 80 <= grade <= 89:
    print("BA")
elif 70 <= grade <= 79:
    print("BB")
elif 60 <= grade <= 69:
    print("CB")
elif 50 <= grade <= 59:
    print("CC")
elif 0 <= grade <= 49:
    print("FF")
    print("Seneye artık")
else:
    print("Geçerli bir not giriniz.")
    

# Soru 8

# Aşağıdaki değişken tanımlıdır.

# text = "Python programlama dili"

# Aşağıdaki işlemleri gerçekleştiriniz.

# İlk karakteri yazdırınız.
# Son karakteri yazdırınız.
# İlk 6 karakteri yazdırınız.
# Metni ters çevirerek ekrana yazdırınız.

text = "Python programlama dili"
print(text[0])  # İlk karakter
print(text[-1])  # Son karakter
print(text[:6])  # İlk 6 karakter
print(text[::-1])  # Metni ters çevirerek ekrana yazdırma
# Soru 9

# Aşağıdaki değişkenler verilmiştir.

# x = 25
# y = 15

# Karşılaştırma operatörlerini kullanarak aşağıdaki sonuçları ekrana yazdırınız.

# x == y
# x != y
# x > y
# x < y
# x >= y
# x <= y

x = 25
y = 15
print(x == y) 
print(x != y)
print(x > y) 
print(x < y)
print(x >= y)
print(x <= y)


# Soru 10

# Kullanıcıdan ad ve soyad bilgilerini ayrı ayrı alınız.

# f-string kullanarak ad ve soyadı tek bir değişkende birleştiriniz.
# Oluşturulan metni büyük harfe çevirerek ekrana yazdırınız.
# Oluşan metnin uzunluğunu (len) ekrana yazdırınız.

fname = input("Adınızı giriniz: ")
lname = input("Soyadınızı giriniz: ")
full_name = f"{fname} {lname}"
print(full_name.upper())
print(len(full_name))
