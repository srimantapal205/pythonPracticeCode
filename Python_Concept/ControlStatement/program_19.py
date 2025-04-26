#To Display stars in right tringular form.
for i in range(1, 11): #To display 10 row
    #print(i)
    for j in range(1, i-1): #No. of stars = row number
        print('* ', end='')
    print()