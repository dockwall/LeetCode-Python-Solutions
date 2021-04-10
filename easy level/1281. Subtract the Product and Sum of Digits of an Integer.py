"""
Problem:
Given an integer number "n",
return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21

Constraints:
1 <= n <= 10^5
"""

number1 = 234                          # First example
number2 = 4421                         # Second example


# If you want to simplify this code, you can use "map()" system function
def subtractProductAndSum(n):
    func_string = str(n)               # Change "int" type to "str"
    func_list = []                     # Create empty list for function

    for text_number in func_string:    # Iterating over elements in string number
        int_number = int(text_number)  # Convert each element to "int" type
        func_list.append(int_number)   # Add each "int" type element in list

    product = 1                        # Default product
    for number in func_list:
        product *= number              # Multiply all numbers

    summary = 0
    for number in func_list:
        summary += number              # Add all numbers

    output = product - summary         # Difference between product and summary
    return output


print('First number:', number1)
print('Product of Subtract and Sum:', subtractProductAndSum(number1), '\n')

print('Second number:', number2)
print('Product of Subtract and Sum:', subtractProductAndSum(number2))
