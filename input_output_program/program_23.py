#To find the power value of a number 
import argparse

#Call the Argumentparser()
parser = argparse.ArgumentParser()

#Add the arguments into args object
args = parser.add_argument('num', nargs='+')

#Retrive the arguments into args object 
args = parser.parse_args()

#Display the arguments from the list: args.nums for x in args.num

for x in args.num:
    print(x)
    