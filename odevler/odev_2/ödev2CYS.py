# Python Collections – 10 Uygulama Sorusu
# 1. Listeye Eleman Ekleme ve Güncelleme

# Aşağıdaki kullanıcı listesini oluşturunuz:

# users = ["Ali", "Veli", "Ayşe", "Fatma", "Mehmet"]

# Programınız;

# Listenin elemanlarını ekrana yazdırmalı,
# Listenin uzunluğunu göstermeli,
# Listenin sonuna "Zeynep" eklemeli,
# Listenin 2. index'ine "Ahmet" eklemeli,
# "Fatma" isimli kullanıcıyı silmeli,
# İlk kullanıcıyı "Kemal" olarak güncellemeli,
# Son haliyle listeyi ekrana yazdırmalıdır.
print("--------------1111111111111------------------------")
users = ["Ali", "Veli", "Ayşe", "Fatma", "Mehmet"]

print(users)
print(len(users))
users.append("Zeynep")
users.insert(2,"Ahmet")
users.remove("Fatma")
users[0] = "Kemal"
print(users)

# 2. Liste ve For Döngüsü

# Aşağıdaki listeyi kullanınız:

# numbers = [12, 5, 8, 21, 4, 17, 30, 9, 6]

# Bir for döngüsü kullanarak;

# Listedeki tüm sayıları yazdırınız.
# Sadece çift sayıları yazdırınız.
# Sadece 10'dan büyük sayıları yazdırınız.
# Listedeki sayıların toplamını hesaplayınız.
# Listenin kaç elemandan oluştuğunu bulunuz.

# Sonuçları anlaşılır mesajlarla ekrana yazdırınız.
print("--------------2222222222222------------------------")

numbers = [12,5,8,21,4,17,30,9,6]
for i in range(len(numbers)):
    print(f"liste elemanı:{numbers[i]}")

for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        print(f"liste çift eleman: {numbers[i]}")

for i in range(len(numbers)):
    if numbers[i]>10:
        print(f"liste 10dan büyükler: {numbers[i]}")

print(f"liste toplamı: {sum(numbers)}")

print(f"eleman sayısı: {len(numbers)}")

# 3. range, break ve continue

# range() kullanarak 1 ile 20 arasındaki sayıları dolaşan bir program yazınız.

# Program;

# 5'in katlarını ekrana yazdırmamalı (continue),
# 17 sayısına ulaştığında döngüyü sonlandırmalı (break),
# Diğer sayıları ekrana yazdırmalıdır.

# Örneğin çıktı içerisinde 5, 10, 15 bulunmamalı ve 17 ekrana yazdırılmamalıdır.

print("---------------------333333333333333------------------------")

for i in range(1,20):
    if i%5 == 0:
        continue
    if i == 17:
        break
    print(i)

# 4. While ile Liste İşlemleri

# Aşağıdaki listeyi kullanınız:

# numbers = [10, 25, 7, 32, 18, 41, 6]

# while döngüsü kullanarak listedeki elemanları tek tek ekrana yazdırınız.

# Programınız ayrıca;

# Kaç tane eleman olduğunu,
# Kaç tane çift sayı bulunduğunu,
# Kaç tane tek sayı bulunduğunu

# hesaplayıp ekrana yazdırmalıdır.

# Bu soruda for döngüsü kullanmayınız.

print("----------------------4444444444444444444--------------------------------------")
counter=0
evencount=0
oddcount=0
numbers = [10, 25, 7, 32, 18, 41, 6]
while counter < len(numbers):  
    print(f"while liste elemanları: {numbers[counter]}")
    if numbers[counter] % 2 == 0:
        evencount += 1
    else:
        oddcount += 1
    counter += 1

print("Eleman sayısı: " + str(len(numbers)))
print(f"Çift eleman sayısı: {evencount}")
print(f"Tek eleman sayısı: {oddcount}")


# 5. Liste İçerisindeki Dictionary Yapısı

# Aşağıdaki şehir listesini oluşturunuz:

# cities = [
#     {"name": "Istanbul", "population": 15000000, "area": 5461},
#     {"name": "Ankara", "population": 5500000, "area": 2512},
#     {"name": "Izmir", "population": 4300000, "area": 1234},
#     {"name": "Bursa", "population": 3000000, "area": 1050}
# ]

# Bir for döngüsü kullanarak;

# Her şehrin adını,
# Nüfusunu,
# Yüzölçümünü

# ekrana yazdırınız.

# Daha sonra programı geliştirerek nüfusu 5.000.000'dan fazla olan şehirleri ayrıca listeleyiniz.

print("----------------------55555555555555---------------------")

cities = [
    {"name": "Istanbul", "population": 15000000, "area": 5461},
    {"name": "Ankara", "population": 5500000, "area": 2512},
    {"name": "Izmir", "population": 4300000, "area": 1234},
    {"name": "Bursa", "population": 3000000, "area": 1050}
]

for city in cities:
    print(f"Name : {city["name"]}" + f" Population : {city["population"]}" + f" Area : {city["area"]}")

print("nüfusu 5.000.000'dan fazla olan şehirler")
for city in cities:
    if city["population"] > 5000000:
        print(f"Name : {city["name"]}" + f" Population : {city["population"]}" + f" Area : {city["area"]}")

# 6. Liste Sıralama ve Tersine Çevirme

# Aşağıdaki kullanıcı listesini kullanınız:

# users = ["Ahmet", "Mehmet", "Fatma", "Ayşe", "Zeynep", "Bengü"]

# Programınız;

# Listenin mevcut halini yazdırmalı,
# Listeyi alfabetik olarak sıralamalı,
# Sıralanmış listeyi yazdırmalı,
# Listeyi tersine çevirmeli,
# Son halini yazdırmalı,
# Listenin ilk ve son elemanını ayrıca göstermelidir.

# sort() ve reverse() metotlarını kullanınız.

print("----------------------66666666666666---------------------")

users = ["Ahmet", "Mehmet", "Fatma", "Ayşe", "Zeynep", "Bengü"]

print(f"listenin mevcut hali: {users}")

users.sort()
print(f"listenin alfabetik sıralı hali: {users}")

users.reverse()
print(f"listenin ters sıralı hali: {users}")

print(f"Listenin ilk elemanı: {users[0]} Listenin son elemanı: {users[-1]}")

# 7. Tuple ve Set Kullanımı

# Aşağıdaki gün listesini oluşturunuz:

# days = (
#     "Pazartesi",
#     "Pazartesi",
#     "Salı",
#     "Çarşamba",
#     "Çarşamba",
#     "Perşembe",
#     "Cuma",
#     "Cumartesi",
#     "Pazar"
# )

# Programınız;

# Tuple'ın tamamını yazdırmalı,
# İlk günü göstermeli,
# Tuple'ın kaç elemandan oluştuğunu bulmalı,
# Tuple'ı set yapısına dönüştürmeli,
# Set içerisindeki benzersiz günleri yazdırmalıdır.

# Ayrıca tuple içerisindeki tekrar eden günlerin neden set içerisinde tek bir kez bulunduğunu gözlemleyiniz.

print("----------------------77777777777777---------------------")
days = (
    "Pazartesi",
    "Pazartesi",
    "Salı",
    "Çarşamba",
    "Çarşamba",
    "Perşembe",
    "Cuma",
    "Cumartesi",
    "Pazar"
)

print(f"tuple tamamı: {days}")
print(f"ilk gün: {days[0]}")
print(f"eleman sayısı: {len(days)}")
set_days = set(days)
print(f"set hale gelmis veri:  {set_days}")

# 8. Dictionary Üzerinde İşlemler

# Aşağıdaki dictionary yapısını oluşturunuz:

# user = {
#     "name": "Ahmet",
#     "age": 30,
#     "city": "Istanbul"
# }

# Programınız;

# Kullanıcının adını,
# Yaşını,
# Şehrini

# ekrana yazdırmalıdır.

# Daha sonra;

# "email" anahtarını ekleyiniz,
# Kullanıcının adını "Mehmet" olarak değiştiriniz,
# Yaşını 35 olarak güncelleyiniz,
# "address" anahtarını ekleyiniz.

# Son olarak dictionary'nin;

# keys() değerlerini,
# values() değerlerini,
# Eleman sayısını

# ekrana yazdırınız.

print("----------------------8888888888888---------------------")
user = {
    "name": "Ahmet",
    "age": 30,
    "city": "Istanbul"
}

print(f"name: {user['name']} " + f"age : {user["age"]} "+ f"city : {user['city']}")
user["email"] = "a@a.com"
user["name"] = "Mehmet"
user["age"] = 35
user["address"] = "abc sk."

print(user)

print(f"keys: {user.keys()}")
print(f"value: {user.values()}")
print(f"eleman sayısı:  {len(user)}")

# 9. Dictionary Listesi ile Kullanıcı Arama

# Aşağıdaki yapıyı kullanınız:

# users = [
#     {"name": "Ahmet", "age": 30, "city": "Istanbul"},
#     {"name": "Mehmet", "age": 25, "city": "Ankara"},
#     {"name": "Ayşe", "age": 20, "city": "Izmir"},
#     {"name": "Fatma", "age": 35, "city": "Bursa"}
# ]

# Bir program yazınız.

# Program;

# Tüm kullanıcıları ad, yaş ve şehir bilgileriyle listelemeli,
# Yaşı 30 ve üzeri olan kullanıcıları göstermeli,
# "Ankara" şehrinde yaşayan kullanıcıları göstermeli,
# "Ayşe" isimli kullanıcıyı bulduğunda "Ayşe bulundu" mesajını yazdırmalıdır.

# Kullanıcı arama işleminde for ve break kullanınız.

print("----------------------999999999999---------------------")
users = [
    {"name": "Ahmet", "age": 30, "city": "Istanbul"},
    {"name": "Mehmet", "age": 25, "city": "Ankara"},
    {"name": "Ayşe", "age": 20, "city": "Izmir"},
    {"name": "Fatma", "age": 35, "city": "Bursa"}
]
for user in users:
    print(f"name: {user['name']} age: {user['age']} city: {user['city']} ")    
print("---------------------")

print("yaşı 30 ve dan büyük olanlar")
for user in users:
    if user["age"]>=30:
        print(f"name: {user['name']} age: {user['age']} city: {user['city']} ")  



for user in users:
    if user["city"] =="Ankara":
        print(f"name: {user['name']} age: {user['age']} city: {user['city']} ")    

for user in users:
    if user["name"] == "Ayşe":
        print("ayşe bulundu and break çalışır")
        break

# 10. Kapsamlı Collections Uygulaması

# Bir şirketin çalışanlarını aşağıdaki yapıda tutan programı yazınız:

# employees = [
#     {"name": "Ahmet", "department": "Yazılım", "age": 30},
#     {"name": "Mehmet", "department": "Satış", "age": 25},
#     {"name": "Ayşe", "department": "Yazılım", "age": 28},
#     {"name": "Fatma", "department": "İK", "age": 35},
#     {"name": "Zeynep", "department": "Yazılım", "age": 24}
# ]

# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Tüm çalışanları ekrana yazdırınız.
# Sadece "Yazılım" departmanında çalışanları gösteriniz.
# Yaşı 30 ve üzeri olan çalışanları gösteriniz.
# Çalışanların yaşlarını ayrı bir list içerisinde toplayınız.
# Departman isimlerini ayrı bir set içerisinde tutunuz.
# En az bir çalışan "Yazılım" departmanında bulunduğunda "Yazılım departmanı mevcut" mesajını gösteriniz.
# "Fatma" isimli çalışan bulunduğunda aramayı break ile sonlandırınız.
# Çalışan sayısını len() kullanarak gösteriniz.
# Departman listesindeki benzersiz departmanları gösteriniz.
# Programın sonunda çalışanların bilgilerini düzenli ve okunabilir bir biçimde ekrana yazdırınız.

# Ek şart: Bu soruyu çözerken for, if, break, list, set ve dictionary yapılarını birlikte kullanınız.

print("----------------------10101010101010101010---------------------")
employees = [
    {"name": "Ahmet", "department": "Yazılım", "age": 30},
    {"name": "Mehmet", "department": "Satış", "age": 25},
    {"name": "Ayşe", "department": "Yazılım", "age": 28},
    {"name": "Fatma", "department": "İK", "age": 35},
    {"name": "Zeynep", "department": "Yazılım", "age": 24}
]

print(employees)

print("-------------------")
for employee in employees:
    if employee["department"] == "Yazılım":
        print(employee)

print("-------------------")
for employee in employees:
    if employee["age"] >= 30:
        print(employee)

age_array = []
for employee in employees:
    age_array.append(employee["age"])
print(age_array)

department_array = []
for employee in employees:
    department_array.append(employee["department"])  
department_set = set(department_array) 
print(department_set)

print("-------------------")
for employee in employees:
    if employee["department"] == "Yazılım":
        print("yazılım departmanı mevcut")
        break
print("-------------------")
for employee in employees:
    if employee["name"] == "Fatma":
        print("fatma bulundu")
        break

print("-------------------")
print(f"çalışan sayısı: {len(employees)}")

for x in employees:
    print(f"name : {x["name"]}, department: {x["department"]}, age : {x["age"]}")


# print("------------------------")  Anlatmak için yazıldı
# print(users)
# dictuser = users[0]
# dictuser2 = users[1]

# print(dictuser)
# for user in users:
#     if user["age"]>=30:
#         print("yaş30")

# if dictuser["age"]>=30:
#     print("yaş 30")
# if dictuser2["age"]>=30:
#     print("yaş 30")    

# for i in users:
#     if i["name"]=="Ayşe":
#         print("Ayşe Bulundu")
#         break

# count = 0
# for count in range(len(users)):
#     if users[count]["name"]=="Ayşe":
#         print("Ayşe Bulundu bizim countlu")
#         break    

# if users[0]["name"]=="Ayşe":
#     print("Ayşe Bulundu")

# if users[1]["name"]=="Ayşe":
#     print("Ayşe Bulundu")
    
# if users[2]["name"]=="Ayşe":
#     print("Ayşe Bulundu")
    
# if users[3]["name"]=="Ayşe":
#     print("Ayşe Bulundu")    
       
