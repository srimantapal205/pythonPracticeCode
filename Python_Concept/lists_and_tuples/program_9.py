#A python program to find the common element and unique element in to two list
#take two list
lst1 = ['Vinay', 'Krishna', 'Saraswati', 'Govind']
lst2 = ['Rosy', 'Govind', 'Tanushri', 'Vinay', 'Vishal']

print(lst1)
print(lst2)
print()

#convert them into set
s1 = set(lst1)
s2 = set(lst2)

#find the intersection of two sets
s3 = s1.intersection(s2)


#convert the resualtant set into a list
common = list(s3)

#display the list
print('Set of intersection list')
print(common) #['Vinay', 'Govind']
print()

#find the union of two sets
print('Set of union list')
s4 = s1.union(s2)

#display the list
uniValue = list(s4)
print(uniValue) #['Saraswati', 'Govind', 'Tanushri', 'Vinay', 'Vishal', 'Rosy', 'Krishna']
print()
