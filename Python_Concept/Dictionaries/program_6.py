#A pythomn program to show the usage of for loop to retrive elements of dictionary
#using for loop dictionary
colors = {'r':'Red', 'g':'Green', 'b':'Blue', 'w':'White'}

#display only key
for k in colors:
    print(k)

#display only value and pass there key
for k in colors:
    print(colors[k])

#item() method returns  key and value pair into k, v
for k, v in colors.items():
    print('Key == {} : Value :: {}'.format(k,v))

