#Create a python program to accept and display a group of number

strInput = input("Enter numbers seperated by space :: ")

#cut the string where a space is found
lst = strInput.split(' ')

#Display the numbers from the list 
for i in lst:
    print(i)