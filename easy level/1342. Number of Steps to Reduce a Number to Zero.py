"""
Problem:
Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:
Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:
Input: num = 8
Output: 4
Explanation:
Step 1) 8 is even; divide by 2 and obtain 4.
Step 2) 4 is even; divide by 2 and obtain 2.
Step 3) 2 is even; divide by 2 and obtain 1.
Step 4) 1 is odd; subtract 1 and obtain 0.

Example 3:
Input: num = 123
Output: 12

Constraints:
0 <= num <= 10^6
"""

num1 = 14                      # First example
num2 = 8                       # Second example
num3 = 123                     # Third example


def numberOfSteps(num):
    steps = 0                  # Quantity of steps
    while num != 0:            # While "num" is not 0
        if num % 2 == 0:       # If "num" is even, divide "num" by 2 and increase "steps" by 1
            num /= 2
            steps += 1
        else:                  # If "num" is odd, decrease "num" by 1 and increase "steps" by 1
            num -= 1
            steps += 1
    return steps


print('First number:', num1)
print('Number of steps to reduce to zero:', numberOfSteps(num1), '\n')

print('Second number:', num2)
print('Number of steps to reduce to zero:', numberOfSteps(num2), '\n')

print('Third number:', num3)
print('Number of steps to reduce to zero:', numberOfSteps(num3))
