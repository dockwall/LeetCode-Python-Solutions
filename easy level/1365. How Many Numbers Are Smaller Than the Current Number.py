"""
Problem:
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's
such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
1)2 <= nums.length <= 500
2)0 <= nums[i] <= 100
"""

nums1 = [8, 1, 2, 2, 3]               # First example
nums2 = [6, 5, 4, 8]                  # Second example
nums3 = [7, 7, 7, 7]                  # Third example


def smallerNumbersThanCurrent(nums):
    output_list = []                  # Array with count of smaller numbers for each number
    for left_num in nums:             # Iterate over left number in "left_num: right_num" pair
        count_smaller = 0             # Count of number, less than left number
        for right_num in nums:        # Iterate over all numbers for left number
            if left_num > right_num:  # Checks if the right number is less than the left number
                count_smaller += 1    # If yes, increase count by 1
            else:
                continue              # If no, go to the next right number
        output_list.append(count_smaller)
        # Writing "count" to an array after checking one left number, moving on to the next
    return output_list


print('First array:', nums1)
print('List of smaller nums:', smallerNumbersThanCurrent(nums1), '\n')

print('Second array:', nums2)
print('List of smaller nums:', smallerNumbersThanCurrent(nums2), '\n')

print('Third array:', nums3)
print('List of smaller nums:', smallerNumbersThanCurrent(nums3))
