"""
Question 4
Group Name: DAN/EXT 55
Group Members:
Thuy Chuong Duong - S385201
Kar Keat Koh - S394886
Joshua Joseph Bargamento - S394292
Sihao Cui - S399370
"""
# Input 
sentence = input("Please enter a sentence: ")

# 1.
# Split 
words = sentence.split()
total_words = len(words)

# 2.
# Max 
# Length :
if words:
    longest_word = max(words, key=len)
else:
    longest_word = "None"

# 3

upper_case = sentence.upper()

# Lowercase
lower_case = sentence.lower()

# Title Case 
title_case = sentence.title()

# Reversed

reversed_sentence = sentence[::-1]

# (Display Results)
print("\n--- Analysis Results ---")
print(f"Total words: {total_words}")
print(f"Longest word: {longest_word}")
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
print(f"Title case: {title_case}")
print(f"Reversed: {reversed_sentence}")
