#Search for an element in a list
group1 = [0,1,2,3,4,5,6,7,8,9] #Create a list of item.
srchItem = int(input("Enter a search element: ")) #Input the search item
for element in group1:
    if srchItem == element:
        print('Element Found in the Group')
        break
else:
    print("Element not found in the group")