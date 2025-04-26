#Find the number of word in a string
str = input('Enter a string :: ')
i=c=0
flag = True #This is becomes False when no space is found
for s in str:
    #count only when there in no space previously
    if flag == False and str[i] == ' ':
        c+=1
    #if space is found take flag as True
    if str[i] == ' ':
        flag = True
    else:
        flag = False
    i+=1
print('No. of Words :: ', c+1)