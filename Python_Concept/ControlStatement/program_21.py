#To Display stars in equilatteral triangular form
n=40
for i in range(1,11):
    #print(i)
    print(' '*n, end="")
    print('* '*(i))
    n-=1
    

for x in range(1,11):print("* "*(x))


for y in range(1, 11):
    print(" "*y, end="")
    print("* "*(y))
    
for m in range(1,11):
    #print(' '*(n-1) + '* '*(m))
    print(' '*(n-m) + '* '*(m))