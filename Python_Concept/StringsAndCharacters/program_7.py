#A program to display all possition of a sub string in a given  main string :: V2
mainStr = input('Enter main string :: ')
subStr = input('Enter sub string :: ')

flag = False
pos =-1
n = len(mainStr)

while True: #Repeat forver
    pos = mainStr.find(subStr, pos+1, n)
    if pos == -1:
        break
    print('Found at positin :: ', pos+1)
    flag= True
    
if flag==False:
    print("Not Found")

#Number of sub string Count
n = mainStr.count(subStr)
print(n)

#Count Repeat character count
reptCharacter =  input("Enter a character for count :: ")
rn = mainStr.count(reptCharacter)
print(rn)