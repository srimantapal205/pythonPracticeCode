#Aoython progrm to sort a tuple with nested tuple
#take emplue tuple with id number , name, salary 

emp = ((10, "Vijay", 9000.50), (20, "Nihaar", 5500.45),(30, "Vanaja", 8900.40),(40, 'Kapoor', 5000.46))
print(sorted(emp)) #Sorted by default on id
print(sorted(emp, reverse=True)) #Reversed on id
print(sorted(emp, key=lambda x:x[1]))#Sort on name
print(sorted(emp, key=lambda x:x[2]))#Sort on salry