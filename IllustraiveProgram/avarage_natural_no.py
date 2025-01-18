'''
Write a program to the avarage of N natural number where the value of N is enterdf the value of N is enterd through keyboard.

'''

num = int(input('Enter the number: '))
def findAvg(n):
    sum = 0
    for num in  range(1, n+1):
        print(num)
        sum = sum + num
        print(sum)
    avg = float(sum/n)
    print('Sum = ', sum)
    return avg

print('Avarage of', num, 'natural numbers = ', findAvg(num)) 
