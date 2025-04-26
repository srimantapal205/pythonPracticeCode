#Write a program that returns the chinese zodic sign of a person where year of birth is entered through keyboard.

def findZodic(year):
    if year % 12 == 1:
        return 'Roaster'
    elif year % 12 == 2:
        return 'Dog'
    elif year % 12 == 3:
        return 'Pig'
    elif year % 12 == 4:
        return 'Rat'
    elif year % 12 == 5:
        return 'Ox'
    elif year % 12 == 6:
        return 'Tiger'
    elif year % 12 == 7:
        return 'Hare'
    elif year % 12 == 8:
        return 'Dragon'
    elif year % 12 == 9:
        return 'Snake'
    elif year % 12 == 10:
        return 'Horse'
    elif year % 12 == 11:
        return 'Sheep'
    elif year % 12 == 0:
        return 'Monkey'
while  True:
    year = int(input('Enter your year of birth : '))
    print('You are born in the year :', year)
    print('Your chinese Zodiac Animal is : ', findZodic(year))
    ch = input('Enter Y to continue and N to exit : ')
    if ch == 'n' or ch == "N":
        print('You optd to exit')
        break
    
    
    
    
    