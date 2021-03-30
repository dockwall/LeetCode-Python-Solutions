"""
Problem:
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
The given address is a valid IPv4 address.
"""

address1 = "1.1.1.1"  # First example
address2 = "255.100.50.0"  # Second example


def defangIPaddr(address):
    output_address = address.replace('.', '[.]')  # Using the .replace method to replace with a template
    return output_address  # Return output string


print('Initial address 1:', address1)
print('Defanged address 1:', defangIPaddr(address1), '\n')

print('Initial address 2:', address2)
print('Defanged address 2:', defangIPaddr(address2))
