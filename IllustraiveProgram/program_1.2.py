# R-1.2 Write a short Python function, is_even (k), that takes an integer value and retums True if k is even, and False otherwise. However, your function cannot use the multiplication. modulo, or division operator.

def is_even (k):
    return (k & 1) == 0

print(is_even(4))
print(is_even(5))
print(is_even(6))


