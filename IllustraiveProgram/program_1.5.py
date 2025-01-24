# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python's comprehension syntax and the built-in sum function.
n = 10
evenValue = sum (i**2 for i in range(2, n, 2))

print(evenValue)