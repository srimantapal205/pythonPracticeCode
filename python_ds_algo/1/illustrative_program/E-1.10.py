#Write a program to find the sum of only integer number in list. for noninteger numbers an exception is caught
number =  input('Enter a list of number seperated by space :: ')
num = number.split()
sum = 0;
for n in num:
    try:
        intnum = int(n)
        sum = sum+intnum
    except ValueError:
        print('Enter could not be converted to integer. Not valid! ', n)
print('Sum of the valis integer number :: ', sum )