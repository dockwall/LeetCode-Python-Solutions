"""
Problem:
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer
has in the j-th bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

Constraints:
1)m == accounts.length
2)n == accounts[i].length
3)1 <= m, n <= 50
4)1 <= accounts[i][j] <= 100
"""

accounts1 = [[1, 2, 3], [3, 2, 1]]             # First example
accounts2 = [[1, 5], [7, 3], [3, 5]]           # Second example
accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]  # Third example


def maximumWealth(accounts):
    biggest_wealth = 0                         # Variable for the biggest customer's wealth
    for i in accounts:                         # Loop to iterate over customers
        customer_wealth = 0                    # Variable for the wealth of current customer
        for j in i:                            # Loop to iterate over banks in the current customer
            customer_wealth += j               # Count the amount
        if biggest_wealth < customer_wealth:   # If the current consumer has more money -
            biggest_wealth = customer_wealth   # Then rewrite the biggest wealth
        else:
            continue                           # If not - go to the next customer
    return biggest_wealth


print('First grid of accounts:', accounts1)
print('The biggest wealth:', maximumWealth(accounts1), '\n')

print('Second grid of accounts:', accounts2)
print('The biggest wealth:', maximumWealth(accounts2), '\n')

print('Third grid of accounts:', accounts3)
print('The biggest wealth:', maximumWealth(accounts3))
