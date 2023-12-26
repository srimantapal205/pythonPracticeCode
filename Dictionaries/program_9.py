#Apython program to conver the elements of two list in to key value pairs of a dictionary
#Converting list in to dictionary
#take two seperate list with elements 
countries =["India","USA","Germany","France"]
cities = ['New Delhi', 'Washington', 'Berlin', 'Paris']

#make a dictionary
z = zip(countries,cities)
d =dict(z)

#Display key and value paris from dictionary d
print('{:15s} -- {:15s}'.format('Country','Capital'))
for k in d:
    print('{:15s} -- {:15s}'.format(k, d[k]))
     

