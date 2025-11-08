"""
Soru: Dört milyonu (4,000,000) aşmayan Fibonacci dizisi terimlerini göz önüne alarak, çift değerli terimlerin toplamını bulun.

ALGORİTMA
1- Boş liste oluşturulur.
2- Üst sınır belirlenir
3- Öncelikle sayıların Fibonacci dizisinde olup olmadığına bakılır.
4- Bunun için 1 ve 2 sayıları başlangıç değerleri olarak kabul edilir.
5- İki farklı değişken oluşturulur, 1 ve 2 değerleri bu değişkenlere sırasıyla atanır.
6- İki değişken toplanır.
7- Bulunan sonucun ikiye bölümünden kalan 0 ise sonuç listeye eklenir.
8- İki değişkenden küçük olan değer bulunan sonuç ile değiştirilir.
9- İşlem üst sınırdaki sayıya kadar devam eder.
"""

x = 1
y = 2
sonuc = 0
toplam=0
while sonuc<4000000:
    
    sonuc = x+y
    x,y = y,sonuc
    
    if sonuc % 2 == 0:
        toplam+=sonuc
        

print(toplam+2)
    
