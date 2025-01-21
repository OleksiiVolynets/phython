
person={"name":"Alex","age":17,5:12,True:"False"}
print(person["name"])
print(person[5])
#slownik = {k1 : w1, k2:w2} definiowanie 2 elementowego słownika
#slownik[k1] odwołanie do elementu słownika o kluczu k1
#slownik.keys() zwraca wszystkie klucze
#slownik.values() zwraca wszystkie wartości
#slownik.items() zwraca gotowe pary krotek klucz-wartość
#slownik.update({k3:w3})
#slownik[k4] = w4 dwa sposoby na dodanie elementu do słownika
#del slownik[k4] Usunięcie elementu słownika o wskazanym
person[5]=6
print(person[5])
person1=dict(name="Olek",age=17)
print(person1)
print(person.items())
for key in person:
    print(key)
for key, values in person.items():
    print(key,values,sep="-")
for value in person.values():
    print(value)
#функції які стоюсуються роботи зі словниками
#person.clear() чистить словник
person.popitem() #видаляє останню
person.pop(5)
person["bio"]="plak"#додавання елементу

print(person)
#Великий список
people={
    "user1":{
        "name":"Alex",
        "age":"17",
        "adress":("Lonadon","Andersena5",54678),
        "grades":{"math":12,"programming":12}


    },
    "user2":{
        "surname":"Kane",
        "name":"Elthon"
    }
}
print(people["user1"]["adress"][1])