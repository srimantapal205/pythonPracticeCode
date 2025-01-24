# R-1.1 Write a short Python function, is_multiple(n, m), that takes we integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise. 



def is_multiple(n,m):
    if m == 0:
        return False
    return n%m == 0

print(is_multiple(19,5))
print(is_multiple(6,5))
print(is_multiple(5,5))

'''
The function first checks if m is zero to avoid a division-by-zero error.
It uses the modulus operator % to determine if the remainder of n divided by m is zero.
If the remainder is zero, n is a multiple of m, and the function returns True; otherwise, it returns False.

'''