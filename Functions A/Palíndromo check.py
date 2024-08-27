#Palíndromo check:

def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

text = input("Enter a word or phrase: ")

print(is_palindrome(text))