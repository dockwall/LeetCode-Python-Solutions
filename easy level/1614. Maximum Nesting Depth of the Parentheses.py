"""
Problem:

A string is a valid parentheses string (denoted VPS) if it meets one of the following:
It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:
depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2),
and ")(" and "(()" are not VPS's.
Given a VPS represented as string s, return the nesting depth of s.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

Example 3:
Input: s = "1+(2*3)/(2-1)"
Output: 1

Example 4:
Input: s = "1"
Output: 0

Constraints:
1)1 <= s.length <= 100
2)s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
3)It is guaranteed that parentheses expression s is a VPS.
"""

s1 = "(1+(2*3)+((8)/4))+1"            # First example
s2 = "(1)+((2))+(((3)))"              # Second example
s3 = "1+(2*3)/(2-1)"                  # Third example
s4 = "1"                              # Fourth example


def maxDepth(s):
    max_depth = 0                     # Max depth of nesting
    open_par = 0                      # Amount of opening parentheses
    for symbol in s:                  # Iterate over symbols in input string
        if symbol == '(':
            open_par += 1             # If parenthesis is open, increase amount by 1
            if open_par > max_depth:
                max_depth = open_par  # Nested check: if amount of open > max nesting, increase max by 1
        elif symbol == ')':
            open_par -= 1             # If parenthesis is open, decrease amount by 1
    return max_depth


print('First string:', s1)
print('The nesting depth of string', maxDepth(s1), '\n')

print('First string:', s2)
print('The nesting depth of string', maxDepth(s2), '\n')

print('First string:', s3)
print('The nesting depth of string', maxDepth(s3), '\n')

print('First string:', s4)
print('The nesting depth of string', maxDepth(s4))
