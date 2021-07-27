"""
Problem:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position
to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as
"sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

Given a shuffled sentence "s" containing no more than 9 words, reconstruct and return the original sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in "s" to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:
Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
"""


def sortSentence(s):

    def keyFunc(item):               # Function for key of list.sort method
        return item[-1]

    arr = s.split(" ")               # Create an array of strings
    arr.sort(key=keyFunc)            # Sorting this array with our key

    raw_str = ''                     # Raw string with an extra space

    for word in arr:
        raw_str += word[0:-1] + ' '  # Add word from "arr" to "raw string" without numbers, add space

    output_str = raw_str[0:-1]       # Create an output string without extra space

    return output_str


# First example
s1 = "is2 sentence4 This1 a3"
print(sortSentence(s1))

# Second example
s2 = "Myself2 Me1 I4 and3"
print(sortSentence(s2))
