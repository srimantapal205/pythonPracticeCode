#A python program to create a dictionary that does not change the order of the elements
#Create an orderd dictionary
from collections import OrderedDict
d = OrderedDict() #d is ordered dictionary
d[10] ="A"
d[11] ="B"
d[12] ="C"
d[13] ="D"
d[14] ="E"

#Display the orderd dictionary
for i, j in d.items():
    print(i, ' ---- ',j)
