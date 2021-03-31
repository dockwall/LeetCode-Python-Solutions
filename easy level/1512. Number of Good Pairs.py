"""
Problem:
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,11,]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

nums1 = [1, 2, 3, 1, 1, 3]  # First example
nums2 = [1, 1, 1, 1]  # Second example
nums3 = [1, 2, 3]  # Third example


def numIdenticalPairs(nums):
    quantity = 0  # Output variable defining quantity of good pairs
    current_second_index = 1  # lower bound of right piece current index (more by one)
    for element in nums:  # Loop iterating over numbers (left piece of pair)
        for j in range(current_second_index, len(nums)):
            # Nested loop iterating over all "j" (right piece's index) for each number (left piece)
            # Lower bound - 1 for the first element (i == 0), increases by one for the next element
            # Upper bound - length of input List ("range()" func doesn't take the last element)
            if element == nums[j]:
                quantity += 1  # "element" - left peace of pair, "nums[j]" - right piece of pair
            else:
                continue  # if not, continue with next "j" (right piece's index)
        current_second_index += 1  # Increase lower bound by 1 for next iteration over
    return quantity


print('First nums:', nums1)
print('Good pairs:', numIdenticalPairs(nums1), '\n')

print('Second nums:', nums2)
print('Good pairs:', numIdenticalPairs(nums2), '\n')

print('Third nums:', nums3)
print('Good pairs:', numIdenticalPairs(nums3))
