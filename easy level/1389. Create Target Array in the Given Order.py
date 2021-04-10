"""
Problem:
Given two arrays of integers nums and index.
Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i],
insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.

Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Example 2:
Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

Example 3:
Input: nums = [1], index = [0]
Output: [1]

Constraints:
1)1 <= nums.length, index.length <= 100
2)nums.length == index.length
3)0 <= nums[i] <= 100
4)0 <= index[i] <= i
"""

nums1 = [0, 1, 2, 3, 4]                    # First example
index1 = [0, 1, 2, 2, 1]

nums2 = [1, 2, 3, 4, 0]                    # Second example
index2 = [0, 1, 2, 3, 0]

nums3 = [1]                                # Third example
index3 = [0]


def createTargetArray(nums, index):
    output_list = []                       # For generated list
    i = 0                                  # Index of element in indices
    for num in nums:                       # Iterate over all numbers
        output_list.insert(index[i], num)  # Insert current num into generated list in index[i]
        i += 1                             # Go to next index
    return output_list


print('First numbers:', nums1)
print('First indices:', index1)
print('Generated List:', createTargetArray(nums1, index1), '\n')

print('Third numbers:', nums3)
print('Third indices:', index3)
print('Generated List:', createTargetArray(nums3, index3))
