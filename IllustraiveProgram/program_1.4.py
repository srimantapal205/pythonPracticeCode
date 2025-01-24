# R-1.4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the even positive integers smaller than n.
def sum_of_squares_of_evens(n):
    return sum (i**2 for i in range(2, n, 2))

print(sum_of_squares_of_evens(10))  # Output: 120 (2^2 + 4^2 + 6^2 + 8^2 = 4 + 16 + 36 + 64)
print(sum_of_squares_of_evens(5))   # Output: 20 (2^2 + 4^2 = 4 + 16)
print(sum_of_squares_of_evens(1))   # Output: 0 (no even positive integers smaller than 1)

