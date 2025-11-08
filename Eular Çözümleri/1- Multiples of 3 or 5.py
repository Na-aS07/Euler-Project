"""
Soru: 1000'den küçük ve 3 veya 5'e bölünebilen tüm doğal sayıların toplamını bulun.

ALGORİTMA

1- Üst sınır 1000 olarak belirlenir.
2- Üst sınıra kadar tüm sayılarda verilen işlemler tekrarlanır.
3- Her sayı önce üçe bölünür
4- Eğer sayı üçe bölündüğünde 0 kalanını veriyorsa sayı toplam değerine eklenir ve o sayı için işleme devam edilmez.
5- Eğer kalan sıfırdan farklıysa işleme devam edilir.
6- Eğer sayı beşe bölündüğünde 0 kalanını veriyorsa sayı toplam değerine eklenir
7- Toplam değeri ekrana yazdırılır.

"""

toplam1 = 0

for sayi in range(1,1000):
    if sayi % 3 == 0:
        toplam1+= sayi
    elif sayi %5 == 0:
        toplam1+= sayi
        
print(toplam1)

#DAHA DÜZENLİ HALİ

toplam2 = 0

for sayi in range(1,1000):
    if sayi % 3 == 0 or sayi % 5==0:
        toplam2+= sayi

print(toplam2)

