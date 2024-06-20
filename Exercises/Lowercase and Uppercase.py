text2 = "ABgvddVICJSdkeprsmgn UTPDvndhtuwPOTNRSjfisuRNSUesajdsa"

lowercase_count = 0
uppercase_count = 0

text = input("Type some text: ")

for letter in text:
    if letter.islower():
        lowercase_count += 1
    elif letter.isupper():
        uppercase_count += 1

print("Lowercase: ", lowercase_count)
print("Uppercase: ", uppercase_count)

print("Static Text: ", text2)

for letter in text2:
    if letter.islower():
        lowercase_count += 1
    elif letter.isupper():
        uppercase_count += 1

print("Lowercase of the static text: ", lowercase_count)
print("Uppercase of the static text: ", uppercase_count)

