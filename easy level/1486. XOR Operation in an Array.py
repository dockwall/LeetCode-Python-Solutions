"""
Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

Example 1:
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

Example 2:
Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

Example 3:
Input: n = 1, start = 7
Output: 7

Example 4:
Input: n = 10, start = 5
Output: 2

Constraints:
1)1 <= n <= 1000
2)0 <= start <= 1000
3)n == nums.length
"""

n1 = 5
start1 = 0                                      # First example

n2 = 4
start2 = 3                                      # Second example

n3 = 1
start3 = 7                                      # Third example

n4 = 10
start4 = 5                                      # Fourth example


def xorOperation(n, start):
    list_for_xor = []                           # Empty list for XOR operations ("^" in Python)
    result = 0                                  # Output result of XOR operations

    for element in range(n):                    # Generate list based on input data
        number_for_xor = start + (2 * element)  # Generate number
        list_for_xor.append(number_for_xor)     # Add number to an list

    for value in list_for_xor:                  # XOR operation on each element
        result ^= value

    return result


print('First length:', n1)
print('First start:', start1)
print('Output XOR:', xorOperation(n1, start1), '\n')

print('Second length:', n2)
print('Second start:', start2)
print('Output XOR:', xorOperation(n2, start2), '\n')

print('Third length:', n3)
print('Third start:', start3)
print('Output XOR:', xorOperation(n3, start3), '\n')

print('Fourth length:', n4)
print('Fourth start:', start4)
print('Output XOR:', xorOperation(n4, start4))