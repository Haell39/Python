#Contagem de vogais função:
def count_vowels(string):
  count = 0
  for char in string:
    if char in "aeiouAEIOU":
      count += 1
  return count

text = input("Type a text: ")
print(count_vowels(text))