"""
Problem:

Given two string arrays word1 and word2,
return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1)1 <= word1.length, word2.length <= 103
2)1 <= word1[i].length, word2[i].length <= 103
3)1 <= sum(word1[i].length), sum(word2[i].length) <= 103
4)word1[i] and word2[i] consist of lowercase letters.
"""


def arrayStringsAreEqual(word1, word2):
    str_word1 = ''                       # First word in 'str' type
    str_word2 = ''                       # Second word in 'str' type

    for words in word1:                  # Generate first word
        str_word1 += words

    for words in word2:                  # Generate second word
        str_word2 += words

    if str_word1 == str_word2:           # Comparison of two 'str' type words
        return True
    else:
        return False


# First example:
print('First word: ["ab", "c"].', 'Second word: ["a", "bc"]')
print('Do two arrays represent the same string?', arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), '\n')

# Second example:
print('First word: ["a", "cb"].', 'Second word: ["ab", "c"]')
print('Do two arrays represent the same string?', arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), '\n')

# Third example:
print('First word: ["abc", "d", "defg"].', 'Second word: ["abcddefg"]')
print('Do two arrays represent the same string?', arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
