# Ornek 8.8
# Klavyeden girilen NxN tipindeki A matrisinin tum elemanlarinin toplamini
# hesaplayip ekrana yazdiran program.

# bu fonksiyon verilen matrisin tum elemanlarini toplayip ve yazdiriyor.
# parametreler sirasiyla: deger listesi, kare matrisin tipi(mesela 2x2,3x3,4x4...)
def matris_topla(liste, matris:int)->None:   # return type 'None' cunku bulunan deger
                                             # yazdirilacak fonksiyonun icinde
    T = 0
    for i in range(matris):
        for j in range(matris):
            T += liste[i][j]

    print("Tum matris elemanlarinin toplami {}".format(T))

#matris girme
N=int(input("Kare matrisin tipini giriniz: "))
A=[[[] for i in range(N)] for j in range(N)] # onceki orneklerdeki aciklamalara bkz.
for i in range(N): # satir icin
    for j in range(N): # sutun icin
        A[i][j]=int(input("A(%d,%d= "%(i+1,j+1)))

matris_topla(A,N) # fonksiyon burada ornek olarak cagirildi
