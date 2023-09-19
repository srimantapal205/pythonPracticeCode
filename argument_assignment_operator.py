# Augmented Assignment Operator

some_value = 5
some_value += 2
print(some_value)

#Type Conversion

print(str(100))

#Escape Sequence

weather =  "It's Sunny"

sent = "It\'s \"Kind of \" Sunny"

print(sent)

#formated string
name = "Johnny"
age = 55

print(f'Hi {name}, You are {age} years old')

#Stirng index
text = 'Hi Hello'
print(text[0])
print(text[7])

text2 = '0123456789'
      #  0123456789
      
#[start:stop:stepover]
print(text2)
print(text2[0:10])
print(text2[0:10:2])#bydefault stepover value is 1
print(text2[1:])
print('arr:'+ text2[0:0])
print('arr:'+ text2[:])
print('arr:'+ text2[:5])
print('arr:'+ text2[::1])
print('arr:'+ text2[::2])
print('arr:'+ text2[:2:])
print('arr:'+ text2[-1]) #Last index value of array
print('arr:'+ text2[::-1]) #Revers order of array step 1
print('arr:'+ text2[::-2]) #Revers order of array step 2

#List
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = ['a','b', 1,2,3,True]

amazone_cart = ['notebook', 'Sunglasses']
print(amazone_cart[1])

#list Slicing

amazoneCart = [
      'notebook', 
      'Sunglasses', 
      'toys',
      'grapes'
]

print(amazoneCart)

amazoneCart[0]='laptop'
print(amazoneCart)

newCart = amazoneCart[:] #Copy of array 
newCart[0]= 'gum'
print(newCart)

#Matrix

matrixList = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matrixList[1][2])

#List Methods

basket = [1,2,3,4,5,6]
print(basket)
print(len(basket))

#adding
print(basket.append(7))
#print(basket)
newBasket = basket
print(newBasket)

basket.insert(1,99)
newBasket2 = basket;
print(newBasket2)

basket.extend([101])
newBasket3 = basket;
print(newBasket3)

#Remove

basket.pop()

print(basket)

#List Item Data 
      #Duplicate
thisList = ['apple', 'banana', 'cherry','apple', 'cherry']
print(thisList)

      #list Length
print(len(thisList))

list1 = ['apple', 'banana','cherry']
list2 = [1,2,3,4,5]
list3 = [True, False,True]

list4 = ['apple', 'banana',4,5, True, 6,False]

      #list type
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

      #list constructor
consttList = list((thisList + list2))
print(consttList)

      #Access Lists
print(consttList[2])
print(consttList[-1])
print(consttList[2:6])
print(consttList[:6])
print(consttList[2:])
print(consttList[-5:-1])

newItemList =  ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
newItemList.append("blackcurrant")
sortItem = newItemList
newItemList2 = newItemList
print(newItemList2)

newItemList3 = ["blackcurrant", "watermelon"]
newItemList.extend(consttList)

newlistItem = newItemList
print(newlistItem)

      #remove Item
newlistItem.remove('mango')
print(newlistItem)
print(len(newlistItem))

newlistItem.pop(15) #removes the specified index.
print(newlistItem)
print(len(newlistItem))

newlistItem.pop() #Remove the item from last.
print(newlistItem)
print(len(newlistItem))

clearList =  list1

print(clearList)

clearList.clear() #this method clear the all content from the list but list still remains

print(clearList)


createNewItem = []
createNewItem.extend(newItemList2)
print(createNewItem)

print(createNewItem.count('apple'))


letterList =['a','h','b','r','q','c','t','a', 'i']
letterList.sort()

print(letterList)
print(letterList.count('a'))

numberlist= [5,8,4,6,1,2,4,6,3,8,4,5,6,2,5]
numberlist.sort() #It's return same list with sorted
print(sorted(numberlist)) # it's return new list
print(numberlist)
print(numberlist.count(2))

new_numberlist = numberlist.copy()
print(new_numberlist)
new_numberlist.reverse()
print(new_numberlist)

ace_number = new_numberlist.copy()
ace_number.reverse()
print(ace_number)


print(len(ace_number))

ace_number[::-1]
print(ace_number)

lst_1to100 = range(1,100)
print(list(lst_1to100))

#Dictionary

thisdict = {"brand" : "Ford", "model":"Mustang", "year":1964}
print(thisdict)
print(thisdict['brand'])


thisdict2 = {"brand" : "Ford", "model":"Mustang", "year":1964, "year":2020,}
print(thisdict2)

print(len(thisdict))

thisdict3 ={"brand" : "Ford", "model":"Mustang", "year":1964, "color":["red", "white","blue"]}
print(type(thisdict3))

# dict() Constructor

thisdict4 = dict(name = "John", age = 36, country = "England")

print(thisdict4)
