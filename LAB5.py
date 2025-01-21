#1
import random
def fun():
    print("To jest twoja losowa liczba",random.randint(0,17))
#a=int(input("Liczba 1"))
#b=int(input("Liczba 2"))
fun()
import math
#a
print(pow(81,0.5))
print(pow(8,10))
print(math.sqrt(2)+math.sqrt(3)+math.sqrt(4))
def r(a):
    if a>=0:
        print(math.sqrt(a))
    else:
        print("Hahahaah nie znasz matematyki")
r(-5)
print(pow(125,1/3))
#3
'''import time

def sekundnik(seconds):
    while seconds > 0:
        print(f"Zostało: {seconds}")
        time.sleep(1)
        seconds -= 1
    print("Wszystko")'''


#sekundnik(10) 
#4
import keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("print"))
print(keyword.iskeyword("break"))
print(keyword.iskeyword("done"))
print(keyword.iskeyword("bad"))
#7
def jer(a):
    print("obwod",2*a*math.pi)
    print("pole",math.pi*pow(a,2))
jer(5)