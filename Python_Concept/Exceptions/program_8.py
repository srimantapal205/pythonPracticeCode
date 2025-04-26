#Apython program to handel syntax error given by eval() functon
#example of syntax error
try:
    date = eval(input("Enter date :: "))
except SyntaxError:
    print('Invalid date entered!')
else:
    print('You enterd :: ', date)
    