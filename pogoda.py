from pomiary import c_to_f,predkosc_wiatru,cisnienie_atmosferyczne 
C=25
print(c_to_f(C))
v=10
print(predkosc_wiatru(v))
p=1013
print(cisnienie_atmosferyczne(p))

#B
dni={"dzien1":{"temperatura":20,"prędkość wiatru":15,"ciśnienie atmosferyczne":760}
     ,"dzien2":{"temperatura":40,"prędkość wiatru":30,"ciśnienie atmosferyczne":765},
      "dzien3":{"temperatura":60,"prędkość wiatru":45,"ciśnienie atmosferyczne":770}}
print((dni["dzien1"]["temperatura"]+dni["dzien2"]["temperatura"]+dni["dzien3"]["temperatura"])/3)
#Ocena na 4
#a
'''swownik={}
sk=0
k=0
while 1==1:
    print("Co chcech zrobic: ")
    print("dodać produkt")
    print("usunąć produkt")
    print("Wyświetlić sumaryczną sprzedaż")
    print("Zakończić program")
    a=input("To co chcesz ")
    if a=="dodać produkt":
        b=input("Podaj nazwe produktu ")
        c=input("Jaki był sprzedaż produktu za 3 dni")
        sp=c.split(",")
        print(sp)
        swownik[b]=sp
        print(swownik)
    elif a=="usunąć produkt":
        b=input("Podaj nazwe produktu")
        if b in swownik:
            del swownik[b]
    elif a=="Wyświetlić sumaryczną sprzedaż":
        for i in swownik.values():
            for l in i:
                sk+=int(l)
        print(sk)
    elif a=="Zakończić program":
        break
print(swownik)
#b
a=[]
def licz(j):
    p=0
    for i in j:
        p+=int(i)
    return p
for j in swownik.values():
    k=licz(j)
    a.append(k)
maxim=max(a)
for values,j in swownik.items():
    k=licz(j)
    if k==maxim:
        print(f"dla {values} jest najwięcej sprzedaży")'''
#5
#a
a={'jff': ['4', '8', '6'], 'pojij': ['3', '8', '5']}
def func(a):
    sred=0
    for values,j in a.items():
        p=0
        for i in j:
            p+=int(i)
        sred=p/3
        print(f"dla {values} jest srednia sprzedaż {sred}")
func(a)
#b
s={'jff': ['4', '8', '6'], 'pojij': ['3', '8', '5']}
def konc(s):
    a=float(input("Podaj prog sprzedaży "))
    for values,j in s.items():
        p=0
        for i in j:
            p+=int(i)
        if p>a:
            print(f"dla {values} sumaryczna sprzedaż jest powyżej proga")
        elif p<a:
            print(f"dla {values} sumaryczna sprzedaż jest poniżej proga")
        else:
            print(f"dla {values} sumarycznaa sprzedaż jest równa progowi")
konc(a)