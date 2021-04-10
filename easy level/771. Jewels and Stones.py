"""
Problem:
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have.
Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
1)1 <= jewels.length, stones.length <= 50
2)jewels and stones consist of only English letters.
3)All the characters of jewels are unique.
"""


def numJewelsInStones(jewels, stones):
    quantity = 0                          # Output variable defining quantity of jewels in stones
    for jewel in jewels:                  # Loop iterating over jewel
        for stone in stones:              # Nested loop iterating over all stones for each jewel
            if jewel == stone:
                quantity += 1             # Calculate quantity
            else:
                continue
    return quantity


# First example
print('First Example. Jewels = "aA", stones = "aAAbbbb"')
print('Quantity of Jewels:', numJewelsInStones('aA', 'aAAbbbb'), '\n')

# Second example
print('Second Example. Jewels = "z", stones = "ZZ"')
print('Quantity of Jewels:', numJewelsInStones('z', 'ZZ'))
