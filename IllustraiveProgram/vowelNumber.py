# Write a program that return the number of vowels in a text where the text is enterrd through keyboard.
text = input('Enter your desired text: ')
def countVowels(strTxt):
    count = 0
    for st in strTxt:
        print(st)
        if st == 'a' or st == 'A' or st == 'e' or st == 'E'or st == 'i' or st == 'I' or st == 'o' or st == 'O' or st == 'u' or st == 'U' :
            count += 1
    return count

print(text, countVowels(text))