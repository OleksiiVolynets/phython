#теорія
'''def test():
    print("hello",end="")
    print("!")

test()
test()'''
def test(word):
    print(word,end="")
    print("!")

'''test("tak")
word="home"
test(word)
test("Hi")'''

'''def suma(a,b):
    res=a+b
    test(res)
    return res


res1=suma(5,6)
suma(3.4,5.6)
suma("hi"," world")
print(res1)
#Мінмальний елемент
def minim(p):
    min=p[0]
    for i in p:
        if i<min:
            min=i
    return min


nums1=[5,5,7,8,3,4,2,3,-2]
res1=minim(nums1)

nums2=[5,5,7,8,3,4,2,3,-2,-6]
res2=minim(nums2)
if res1<res2:
    print(res1)
else:
    print(res2)
#lambda
lop=lambda x,y: x*y
print(lop(5,6))'''
def my_function(*a):
    s = 0
    for i in a:
         s += i
    return s
b=my_function(0,0,0)
k=my_function()
print(b)
print(k)
m=my_function(1,2)
print(m)