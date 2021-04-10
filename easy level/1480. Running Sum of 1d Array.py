"""
Problem:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1) 1 <= nums.length <= 1000
2) -10^6 <= nums[i] <= 10^6
"""

nums1 = [1, 2, 3, 4]                      # First example
nums2 = [1, 1, 1, 1, 1]                   # Second example
nums3 = [3, 1, 2, 10, 1]                  # Third example


def running_sum(array):
    output_array = []                     # Create empty List for output
    current_sum = 0                       # Create variable that contains summary of previous elements
    for element in array:                 # This loop iterates over each element in our List
        current_sum += element            # Add the current element to the sum of the previous ones
        output_array.append(current_sum)  # Append current summary to List for output
    return output_array


print('Initial List 1:', nums1)
print('Output List 1:', running_sum(nums1), '\n')

print('Initial List 2:', nums2)
print('Output List 2:', running_sum(nums2), '\n')

print('Initial List 3:', nums3)
print('Output List 3:', running_sum(nums3))
