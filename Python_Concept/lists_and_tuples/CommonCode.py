#Connection of two lists
x = [10,20,30,40,50]
y = [100,110,120]
neLst = x+y
print(neLst)

#Repetition of list
nlst = [10,20,30,40,50,60,70,80,90,100]
print(nlst * 2)

#Membership in list
a = 110
print(a in nlst) #check if a is member of x

#Aliasing and cloning lists
m = [10,20,30,40,50]
n=m # m is aliased as y
print(m) #will display [10,20,30,40,50]
print(n) #will display [10,20,30,40,50]
m[1] = 99 #modify 1st element in x
print(m) #will display [10,99,30,40,50]
print(n) #will display [10,99,30,40,50]

a = [10,20,30,40,50]
b=a[:] # x is cloned as y
print(a) #will display [10,20,30,40,50]
print(b) #will display [10,20,30,40,50]
a[1]=99
print(a) #will display [10,99,30,40,50]
print(b) #will display [10,99,30,40,50]

#list Comprehensions
#v1
squares =[] #create empty list
for i in range(1,11):
    squares.append(i**2)
print(squares)

#v2
squaresV2 = [x**2 for x in range(1, 11)]
print(squaresV2)

#v1
even_squaresV1 = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squaresV1)

#v2
even_squaresV2 = [x**2 for x in range(2, 11, 2)]
print(even_squaresV2)

#If we have two lists x and y and we want to add each element of x with each element of y, we can write for loops as:
x = [10,20,30]
y = [1,2,3,4]
lst=[]
for i in x:
    for j in y:
        lst.append(i+j)
print(lst)

lst_2 = [i+j for i in x for j in y]
print(lst_2)

lst_3 = [i+j for i in [10,20,30] for j in [1,2,3,4]]
print(lst_3)

str_lst = [i+j for i in 'ABC' for j in 'DE']
print(str_lst)

tuf_1 = 1,2,3,4,5
print(type(tuf_1))
lst_5 = [1,2,3,4,5]

tpl_1 = tuple(lst_5)
print(type(tpl_1))
print(tpl_1)

tpl_2 = tuple(range(2, 11, 2))
print(tpl_2)

tpl_3 = (10,20,30,40,50,60,70,80,90,100, 20,)

#Accessing tuple using index
print(tpl_3[0])
print(tpl_3[5])
print(tpl_3[-1])
print(tpl_3[-7])

#Access slicing methods
print(tpl_3[:])
print(tpl_3[1:4])
print(tpl_3[2:11:2])
print(tpl_3[:2])
print(tpl_3[:8:2])
print(tpl_3[::-2])
print(tpl_3[:-2:])

lenTpl = len(tpl_3)
print(lenTpl)

tplMin = min(tpl_3)
print(tplMin)

tplMax = max(tpl_3)
print(tplMax)

tplCount = tpl_3.count(20)
print(tplCount)

tplIndex = tpl_3.index(40)
print(tplIndex)

tpl_sorted = sorted(tpl_3, reverse=True)
print(tpl_sorted)










