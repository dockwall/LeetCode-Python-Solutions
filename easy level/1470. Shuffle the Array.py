"""
Problem:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:
1)1 <= n <= 500
2)nums.length == 2n
3)1 <= nums[i] <= 10^3
"""


def shuffle(nums, n):
    output_array = []               # Output List
    iteration = 1                   # Variable defining iteration
    second_index = n                # Variable defining index y[]
    for element in nums:            # loop iterating over x[]
        if iteration <= n:

            # Variable "n" shows the quantity of x-y pairs
            # One iteration appends one x-y pair
            # Last iteration = last pair
            # Each iteration increases index of "y" and iteration number by 1
            # When iteration > quantity of x-y pairs - return output List

            output_array.append(element)
            output_array.append(nums[second_index])
            second_index += 1
            iteration += 1
        else:

            return output_array


# First example
print('First array: [2, 5, 1, 3, 4, 7], n = 3')
print('Output array:', shuffle([2, 5, 1, 3, 4, 7], 3), '\n')

# Second example
print('Second array: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4')
print('Output array:', shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4), '\n')

# Third example
print('Third array: [1, 1, 2, 2], n = 2')
print('Output array:', shuffle([1, 1, 2, 2], 2))

