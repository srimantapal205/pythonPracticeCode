# Write a program that return the number of vowels in text where the text is enterd through keyboard.

text = input('Enter yor desired text :: ')
def coutVowels(str):
    count = 0
    for st in str:
        if st == 'a' or st == 'A' or \
        st == 'e' or st == 'E' or \
        st == 'i' or st == 'I' or \
        st == 'o' or st == 'O' or \
        st == 'u' or st == 'U': count += 1
    return count
print(text, ', Vowls:: ', coutVowels(text))
        