age = 50
sent = "The best things in life are free!"

newText = "My name is John, I am {}"
print(newText.format(age))


quantity = 3
itemno = 654
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollats."
print(myOrder.format(quantity, itemno, price))

#Using  index numbers to be sure th arguments are placed.
myOrder2 = "I want {2} pieces of item {0} for {1} dollats."
print(myOrder2.format(quantity, itemno, price))

# Python String Methods 

stringText ="in the ever-evolving landscape of web development."

captalize_string = stringText.capitalize() #Convert  the first character to upper case
print(captalize_string)

casefold_text =  captalize_string.casefold() #Convert string into lower case
print(casefold_text)

center_string = stringText.center(80,'O') #Return a centered string
print(center_string)

count_string =  stringText.count("ever-evolving")
print(count_string)

encode_txt = "This is Ståle"
encode_string = encode_txt.encode(encoding="ascii",errors="backslashreplace") #Return Encode string.
print(encode_string)

endwith_string =  stringText.endswith('.') #Returns true if the string ends with the specified value
print(endwith_string)

find_specifie_value = stringText.find("landscape")
print(find_specifie_value)

