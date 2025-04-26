#A function to test whether a number is odd or even

def odd_even(num):
    '''To know the number is Edd or Even'''
    if num % 2 == 0:
        print(num, 'is Even')
    else:
        print(num, 'is Odd')

#Call The function
odd_even(12)
odd_even(12.5)
odd_even(13)
