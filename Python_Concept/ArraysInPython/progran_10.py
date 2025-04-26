#A python program to storing student marks in to an array and finding total marks and percentage ogf marks.

from array import *
#accepting marks as  string
str = input("Enter marks :: ").split(' ')
#store the marks into 'marks' arry
marks = [int(num) for num in str]

#display the marks and fin total
sum = 0
for x in marks:
    print(x)
    sum+=x
print('Total marks: ', sum)

#Display percentage
n=len(marks) #n = no of lement in marks array
percent = sum/n
print("Percentage : ",percent)


    