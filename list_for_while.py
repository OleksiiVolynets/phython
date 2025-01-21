'''nums=[5,3,2,6.6]

for i in nums:
    w=i**2
    print(w)'''

#практичне завдання
user_hobby=int(input("Enter hobby number "))


i=0
hobby=[]
while i< user_hobby:
    text="Enter hobby" +str(i+1)+":"
    hobby.append(input(text))
    i+=1
print(hobby)