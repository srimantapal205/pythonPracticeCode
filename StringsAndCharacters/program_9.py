#A python program to know the type of character entered by user
#to the nature of a character
mainStr = input("Enter a character :: ")
ch = mainStr[0]

#test char
if ch.isalnum():
    print("It is alphabet or numeric character")
    if ch.isalpha():
        print("It is an alphabet")
        if ch.isupper():
            print("It is capital letter")
        else:
            print("It is small letter")
    else:
        print("It is a numeric digit ")
elif ch.isspace():
    print("Its is space")
else:
    print("It's maybe a special character")
