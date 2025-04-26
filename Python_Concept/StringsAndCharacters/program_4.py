#Write a program find first occurrence of sub string in a main string
strTxt = input("Enter main String :: ")
subStr = input("Enter sub string :: ")

#find possition of sub in main string
n = strTxt.find(subStr, 0, len(strTxt)) #search 0 to last characters in the main string

#find(0 returns -1 if sub string is not found)

if n==-1:
    print("Sub string not found")
else:
    print("Sub string found at {} position".format(n+1))