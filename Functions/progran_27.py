# A python program to solve Towers of Hanoi problem.
def towers(n, a, b, c):
    '''this is the Towers of Hanoi problem whre n denote number of disk and a, b, c is a pole'''
    if n == 1:
        #if only 1 disk then move from a to c
        print('Move disk %i from pole %s to pole %s' %(n, a, c))
    else: #more than 1 disk
        #Move first n-1 disk from a to b using c as intermediate pole
        towers(n-1, a, c, b)
        
        #move remaining 1 disk from a to c
        print('Move disk %i from pole %s to pole %s' %(n, a, c))
        
        #move n-1 disk from b to c using a as intermediate pole
        towers(n-1, b, a, c)
        
#call the function 
n = int(input('Enter the number of disk :: '))

#Change the n disk from A to C using B as intermediate pole
towers(n, 'A', 'B', 'C')

        
        
        
'''
Enter the number of disk :: 3
Move disk 1 from pole A to pole C
Move disk 2 from pole A to pole B
Move disk 1 from pole C to pole B
Move disk 3 from pole A to pole C
Move disk 1 from pole B to pole A
Move disk 2 from pole B to pole C
Move disk 1 from pole A to pole C
'''

