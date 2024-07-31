# Write a Python program to count the number of vowels in a given string.

def count_vowels(text):

    count = 0

    for character in text:
        if (character in "aAeEiIoOuU"):
            count += 1

    return count


text = input("Text: ")

count = count_vowels(text)

print("Vowel Counts:", count)
