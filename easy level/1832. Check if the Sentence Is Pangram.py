"""
Problem:
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
"""


def checkIfPangram(sentence):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'  # Constant that consists all English letters (lowercase)
    for letter in ALPHABET:
        if letter in sentence:
            continue                         # If letter in sentence, go next
        else:
            return False                     # If not, False
    return True                              # If all letters in sentence, cool (True)


# First example
sentence1 = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence1))

# Second example
sentence2 = "leetcode"
print(checkIfPangram(sentence2))
