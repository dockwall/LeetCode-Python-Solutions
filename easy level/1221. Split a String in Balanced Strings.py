"""
Problem:
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

Constraints:
1)1 <= s.length <= 1000
2)s[i] is either 'L' or 'R'.
3)s is a balanced string.
"""

balanced_string1 = "RLRRLLRLRL"   # First example
balanced_string2 = "RLLLLRRRLR"   # Second example
balanced_string3 = "LLLLRRRR"     # Third example
balanced_string4 = "RLRRRLLRLL"   # Fourth example


def balancedStringSplit(s):
    result = 0                    # Amount of split balanced strings
    r_count = 0                   # Amount of 'R' symbols
    l_count = 0                   # Amount of 'L' symbols

    for letter in s:              # Iterate over all symbols in input string
        if letter == 'R':
            r_count += 1          # If symbol - 'R', increase amount of 'R' by one
        elif letter == 'L':
            l_count += 1          # If symbol - 'L', increase amount of 'L' by one

        if r_count == l_count != 0:
            result += 1
            # Next check. If amount of 'R' == amount of 'L' and != 0, increase result by 1 and continue

    return result


print('First balanced string:', balanced_string1)
print('Maximum amount of split balanced strings:', balancedStringSplit(balanced_string1), '\n')

print('Second balanced string:', balanced_string2)
print('Maximum amount of split balanced strings:', balancedStringSplit(balanced_string2), '\n')

print('Third balanced string:', balanced_string3)
print('Maximum amount of split balanced strings:', balancedStringSplit(balanced_string3), '\n')

print('Fourth balanced string:', balanced_string4)
print('Maximum amount of split balanced strings:', balancedStringSplit(balanced_string4))
