"""
Problem:
There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1,
such that encoded[i] = arr[i] XOR arr[i + 1].
For example, if arr = [1,0,2,1], then encoded = [1,2,3].
You are given the encoded array.
You are also given an integer first, that is the first element of arr, i.e. arr[0].
Return the original array arr. It can be proved that the answer exists and is unique.

Example 1:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:
Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]

Constraints:
1)2 <= n <= 10^4
2)encoded.length == n - 1
3)0 <= encoded[i] <= 10^5
4)0 <= first <= 10^5
"""

encoded1 = [1, 2, 3]
first1 = 1                     # First example

encoded2 = [6, 2, 7, 3]
first2 = 4                     # Second example


def decode(encoded, first):
    output_original = [first]  # Original array with first number
    index = 0                  # index of original number
    for num in encoded:        # Iterate over numbers in encoded list
        #
        # encoded(index) = original(index) XOR ("^" in Python) original(index + 1)
        # Therefore, original(index + 1) = encoded(index) XOR original(index)
        #
        # It is necessary to create an algorithm
        # That will calculate the next original number, write it down and move on to the next
        #
        original_num = num ^ output_original[index]
        output_original.append(original_num)
        index += 1
    return output_original


print('First encoded List:', encoded1)
print('First element:', first1)
print('Original List', decode(encoded1, first1), '\n')

print('Second encoded List:', encoded2)
print('Second element:', first2)
print('Original List', decode(encoded2, first2))
