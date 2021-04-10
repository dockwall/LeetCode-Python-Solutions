"""
Problem:
You own a Goal Parser that can interpret a string command.
The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o",
and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
Input: command = "(al)G(al)()()G"
Output: "alGalooG"

Constraints:
1)1 <= command.length <= 100
2)command consists of "G", "()", and/or "(al)" in some order.
"""

command1 = "G()(al)"               # First example
command2 = "G()()()()(al)"         # Second example
command3 = "(al)G(al)()()G"        # Third example


# If forbidden to use methods. Can be done roughly with several ".replace" methods in one line
# This line is: command.replace('G', 'G').replace('()', 'o').replace('(al)', 'al')
def interpret(command):
    output_str = ''
    i = 0

    for symbol in command:         # Iterate over all elements in command string
        if symbol == 'G':
            output_str += 'G'
            i += 1
        elif symbol == '(' and command[i + 1] == ')':
            output_str += "o"      # If current symbol = '(' and the next one = ')'
            i += 1
        elif symbol == '(' and command[(i + 1):(i + 4)] == 'al)':  # !Slice's upper bound is not taken
            output_str += 'al'     # If current symbol = '(' and the next three = 'al)'
            i += 1
        else:
            i += 1
    return output_str


print('First string:', command1)
print('Parsed string:', interpret(command1), '\n')

print('First string:', command2)
print('Parsed string:', interpret(command2), '\n')

print('First string:', command3)
print('Parsed string:', interpret(command3), '\n')