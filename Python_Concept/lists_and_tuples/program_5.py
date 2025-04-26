#A python program to understand list processing methods
num = [10,20,30,40,50]
n = len(num)
print('No. Of elements in num :: ', n)

#Append  value
num.append(60)
print('num after appending 60 :: ', num)

#Insertting 5 at 0th opsition
num.insert(0, 5)
print('num  after insertting 5 at 0th opsition:: ', num)

num1 = num.copy()
print('Newly created list num1 :: ', num1)

num.extend(num1)
print('num after appending num1 :: ', num )

n = num.count(50)
print('No. of times 50 found in the list num :: ', n)

num.remove(50)
print('num after removing 50 :: ', num)

num.pop()
print('num after removing ending element :: ', num)

num.sort()
print('num after sorting: ', num )

num.reverse()
print('num after reversing:: ', num)

num.clear()
print('num after removing all elements :: ', num)


