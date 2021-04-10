"""
Problem:
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Example 2:
Input: nums = [1,1,2,3]
Output: [1,3,3]

Constraints:
1)2 <= nums.length <= 100
2)nums.length % 2 == 0
3)1 <= nums[i] <= 100
"""

nums1 = [1, 2, 3, 4]                        # First example
nums2 = [1, 1, 2, 3]                        # Second example


def decompressRLElist(nums):
    output_list = []                        # Create empty decompressed list
    i = 0                                   # Index for list comprehension (LC)
    while i <= (len(nums) - 2):             # The loop runs until the "freq, val" pair is reached
        generated_list = [nums[i + 1] for nums[i] in range(0, nums[i])]
        output_list.extend(generated_list)  # LC for one "freq, val" pair insert result into output list
        i += 2                              # Move on to the next "freq, val" pair
    return output_list


print('First compressed List:', nums1)
print('Decompressed List:', decompressRLElist(nums1), '\n')

print('Second compressed List:', nums2)
print('Decompressed List:', decompressRLElist(nums2))
