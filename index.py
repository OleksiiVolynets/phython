#word="crxrxrux"
#print(list(word))#за допомогою list  можна перетворити
#текстову змінну на список
word=list("tftifiv")
word[0]="Tr"
result="".join(word)#функція "".join(a) пеетворює список на текст
# в лапках з яким інтервалом а-список
print(word)
#result.upper()перетворює всі букви тексту на великі
#result.lower() перетворює всі букви тексту на маленькі
#result.capitalize() перша буква слова велика
result.isupper()# перевіряє чи всі букви великі
result.islower()# перевіряє чи всі букви маленькі
print(result)

#робота з текстом
text="football,basketball,skate"
hobbies=text.split(",")#розбиває текст по символу
print(hobbies)
for i in range(0, len(hobbies)):
    hobbies[i]=hobbies[i].capitalize()
print(hobbies)
result=",".join(hobbies)
print(result)
# індекси та зрізи
lis=[5,3,"Someonre",True,[5,4]]
print(lis[0::2])
print(lis[::-1])
print(lis[:-4:-1])