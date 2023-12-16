#A function that return the result of addition subtraction multiplication and division
def sum_sub_mul_div(a,b):
    '''This function return result of addition, subtraction multiplication and division of a & b'''
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    return c, d, e, f

#Display result using loop
t = sum_sub_mul_div(60, 20)
print('The result :: ')
for i in t:
    print(i, end=" ")
print()   
#Display result individually
n1 = 60
n2 = 20
m, n, o, p = sum_sub_mul_div(n1, n2)

print('The addition of {} & {} :: {}'.format(n1, n2, m))    
print('The subtraction of {} & {} :: {}'.format(n1, n2, n))    
print('The multiplication of {} & {} :: {}'.format(n1, n2, o))    
print('The division of {} & {} :: {}'.format(n1, n2, p))    