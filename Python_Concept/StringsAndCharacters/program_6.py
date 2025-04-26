#Display all position of sub string in the given main string
mainStr = input('Enter main string :: ')
subStr = input('Enter sub string :: ')

i = 0
flag = False
n = len(mainStr)

while i<n:
    pos = mainStr.find(subStr, i, n)
    if pos != -1:
        print("Found at position :: ", pos+1)
        i = pos+1
        flag = True
    else:
        i=i+1
        if flag == False:
            print("Sub srting not found")
        