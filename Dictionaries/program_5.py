#A python prgram to create a dictionary with cricket players name and score in a match. Also we retrive runs by enter palyer's name
#Create a dictionary with cricket playears name with scores
x ={} #take an empty dictionary

print('How many playear\'s ?  ', end='') 
n= int(input())

for i in range(n):
    print('Enter the player name :: ', end='' )
    k = input() # key is string
    print('Enter runs :: ', end='')
    v = int(input())
    x.update({k:v})

print('Displaye All players and score :: ', x)
print()

#Display only players name ::
print('Players in this match:: ')
for pname in x.keys():
    print(pname, end=', ')
print()


#Accept the player name 
print('Enter player name :: ', end='')
plName = input()

#find the runs done by player 
runs = x.get(plName, -1)
if (runs == -1):
    print('Player not found!')
else:
    print('{} made runs {}'.format(plName, runs))


