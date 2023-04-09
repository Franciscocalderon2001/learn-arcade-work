""""LAB 10"""
import re
# separate the two searches
print("--- Linear Search ---")


# split line loop
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = []
# Have it read it line by line
with open("dictionary.txt", "r") as file:
    for line in file:
        dictionary_list.append(line.strip().upper())
# Read AliceInWonderLand text line by line
with open("AliceInWonderLand200.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            if word.upper() not in dictionary_list:
                print(f"Line {line_number} possible misspelled word: {word}")

# Separate the second type of search (optional)
print("--- Binary Search ---")


# binary search loop
def binary_search(word, dictionary_list):
    lower_bound = 0
    upper_bound = len(dictionary_list) - 1
    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        if dictionary_list[middle_pos] < word:
            lower_bound = middle_pos + 1
        elif dictionary_list[middle_pos] > word:
            upper_bound = middle_pos - 1
        else:
            return True
    return False


with open("AliceInWonderLand200.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            if not binary_search(word.upper(), dictionary_list):
                print(f"Line {line_number} possible misspelled word: {word}")
