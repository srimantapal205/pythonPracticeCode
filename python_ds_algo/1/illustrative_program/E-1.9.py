#Write a program to find the number of words in the enterd by the user and then to sort the word.
text = input('Enter some text :: ')
word = text.split() 
count = 0
for w in word:
    count += 1
print('Number of words in the enterd text is : ', count)
word.sort()

print('The words insorted order are : ')
for w in word:
    print(w)