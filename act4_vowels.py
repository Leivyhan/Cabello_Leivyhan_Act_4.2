sentence = input("Sentence: ")
vowels = 0

for ch in sentence:
    if ch in "aeiouAEIOU":
        vowels += 1

print(f"Vowels: {vowels}")