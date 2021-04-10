"""
Problem:
You are given an array items, where each items[i] = [typei, colori, namei]
describes the type, color, and name of the ith item.
You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],
["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"]
and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

Constraints:
1)1 <= items.length <= 10^4
2)1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
3)ruleKey is equal to either "type", "color", or "name".
4)All strings consist only of lowercase letters.
"""

# First example
items1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey1 = "color"
ruleValue1 = "silver"

# Second example
items2 = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey2 = "type"
ruleValue2 = "phone"


def countMatches(items, ruleKey, ruleValue):
    match_count = 0                                        # Count of matches
    for item in items:                                     # Iterate over all items
        if ruleKey == 'type' and ruleValue == item[0]:
            match_count += 1                               # If item type = ruleValue, increase count by 1
        elif ruleKey == 'color' and ruleValue == item[1]:
            match_count += 1                               # If item type = ruleValue, increase count by 1
        elif ruleKey == 'name' and ruleValue == item[2]:
            match_count += 1                               # If item name = ruleValue, increase count by 1
    return match_count


print('First Items:', items1)
print('ruleKey:', ruleKey1, 'ruleValue:', ruleValue1)
print('Found', countMatches(items1, ruleKey1, ruleValue1), 'matched elements\n')

print('First Items:', items2)
print('ruleKey:', ruleKey2, 'ruleValue:', ruleValue2)
print('Found', countMatches(items2, ruleKey2, ruleValue2), 'matched elements')
