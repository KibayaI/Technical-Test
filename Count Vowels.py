# Write a program that counts the number of vowels in a sentence.

sentence = input("Enter your sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = []

sentence = sentence.lower()

for i in range(len(sentence)):
    if sentence[i] in vowels:
        if sentence[i] not in vowel_count:
            vowel_count.append(sentence[i])

print(vowel_count)
print(len(vowel_count))
