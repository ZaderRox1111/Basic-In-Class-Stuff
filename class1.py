def char_freq(char, word):
    return (word.count(char)/len(word))

char = input("What letter do you want to check: ")
word = input("What phrase do you want to check: ")

print(" ")
print(f"The character '{char}' appears in '{word}' at a frequency of: {char_freq(char, word)}")

