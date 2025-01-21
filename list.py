nums=[5,7,4,5.45,6]
nums[0]=34.34
#print(nums[4])

nums2=[5,7,6,[5,"text",True]]
#print(nums2[-1][1])



nums.append(45)#кінець списку
nums.insert(1,False)#після якогось елементу
#nums.extend(nums2)#додає багато елементів
nums.append(5)
nums.append(5)
nums.sort()#сортування
nums.reverse()#перевернення списку
nums.pop()#видаляється останній елемент списка
nums.remove(34.34)#видалити певний елемент
#nums.clear()#видаляється весь список
nums.count(5)#рахує кількість елементів з певним значенням
len(nums)#довжина списку

print(nums)

print(nums.count(5))