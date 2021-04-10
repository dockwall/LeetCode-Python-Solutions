"""
Problem:
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i]
in the shuffled string.
Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Example 3:
Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"

Example 4:
Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"

Example 5:
Input: s = "art", indices = [1,0,2]
Output: "rat"
"""


def restoreString(s, indices):
    output_string = ''  # Create empty string
    for i in range(len(indices)):

        # Iterate over digits from 0 to (length of indices - 1)
        # "i" shows the current character index in a new line

        output_string += s[indices.index(i)]

        # Add letters at indices from 0 to last
        # ".index()" method returns the index of the first occurrence of the given element
        # Example: 0 (first letter) is included in indices under index 4
        # Therefore, first letter of new string contains in "s" under index 4

    return output_string


# First example
print('First string: codeleet')
print('First indices: [4,5,6,7,0,2,1,3]')
print('Shuffled string:', restoreString('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]), '\n')

# Second example
print('Second string: abc')
print('Second indices: [0,1,2]')
print('Shuffled string:', restoreString('abc', [0, 1, 2]), '\n')

# Third example
print('Third string: aiohn')
print('Third indices: [3,1,4,2,0]')
print('Shuffled string:', restoreString('aiohn', [3, 1, 4, 2, 0]), '\n')

# Fourth example
print('Fourth string: aaiougrt')
print('Fourth indices: [4,0,2,6,7,3,1,5]')
print('Shuffled string:', restoreString('aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5]), '\n')

# Fifth example
print('Fifth string: rat')
print('Fifth indices: [1,0,2]')
print('Shuffled string:', restoreString('rat', [1, 0, 2]))
