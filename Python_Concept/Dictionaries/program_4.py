#Apython program to create a dictionary from keyboard and display the elements
#Create a dictionary from the keyboard
x ={}
print('How many element ?', end='')
n=int(input()) #n indicates no. of key-value paires

for i in range(n):
    print('Enter Key :: ', end='')
    k= input() #key is string
    print('Enter value :: ', end='')
    v= int(input()) #value is interger
    x.update({k:v})
#Display the dictionary
print('The dictionary is :: ', x) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

    