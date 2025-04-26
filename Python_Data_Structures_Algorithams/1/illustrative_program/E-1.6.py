#Write a program to find the average of N natural number where the value of N is enterd through keyboard.
num = int(input('Enter the number: '))
def findAvg(n):
    sum = 0
    for num in range(1, n+1):
        print('Number:',  num)
        sum = sum + num
    avg = float( sum/n )
    print('Sum = ', sum)
    return avg
print('Average of ', num, 'natural number = ', findAvg(num))
