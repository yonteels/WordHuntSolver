import sys

# Read in dictionary
def dictionary():
    hashSet = set()
    with open('WordHuntDictionary.txt', 'r') as file:
        for line in file:
            hashSet.add(line.rstrip())
    return hashSet

# Get a subset of the dictionary starting with a specific letter
def quickDictionary(letter, dictionary):
    usable_Dictionary = set()
    for word in dictionary:
        if word.startswith(letter):
            usable_Dictionary.add(word)
    return usable_Dictionary

# Recursive function to find words in the board
def isWord(i, j, arr, currentString, usable_Dictionary, usable_Words, usedPath):
    currentString += arr[i][j]
    key = (i, j)
    usedPath.add(key)

    if currentString in usable_Dictionary:
        usable_Words.add(currentString)

    if any(word.startswith(currentString) for word in usable_Dictionary):
        directions = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1),  # right
            (-1, -1),  # up left
            (-1, 1),  # up right
            (1, -1),  # down left
            (1, 1)   # down right
        ]

        for vert, horo in directions:
            newI, newJ = i + vert, j + horo
            if 0 <= newI < len(arr) and 0 <= newJ < len(arr[0]) and (newI, newJ) not in usedPath:
                isWord(newI, newJ, arr, currentString, usable_Dictionary, usable_Words, usedPath)

    usedPath.remove(key)
    return usable_Words

# Input checker
def isAlph(i, j):
    while True:
        try:
            ui = input(f"Please enter the character for row {i+1}, column {j+1}: ").strip()
            if len(ui) == 1 and ui.isalpha():
                return ui.upper()
            else:
                print("Invalid input. Please enter a single alphabetic character.")
        except Exception as e:
            print(f"Error: {e}. Please re-enter your value.")

# Board initializer
def wordHunt():
    arr = [[0]*4 for _ in range(4)]
    print("Initializing Board")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = isAlph(i, j)
    return arr

# Main code
sys.setrecursionlimit(10000)

# Initialize and create board
Array = wordHunt()

# Initialize dictionary
dictionary = dictionary()

# Find words
all_words = set()
for row in range(len(Array)):
    for col in range(len(Array[0])):
        words_found = isWord(row, col, Array, "", quickDictionary(Array[row][col], dictionary), set(), set())
        all_words.update(words_found)

#sort the word by length
all_words = sorted(all_words, key=len, reverse=True)

print("Found words:", all_words)

print(len(all_words))
