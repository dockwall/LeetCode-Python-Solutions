"""
Problem:
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
КОММЕНТЫ НЕ ЗАБУДЬ СУКА КОММЕНТЫ НЕ ЗАБУДЬ СУКА КОММЕНТЫ НЕ ЗАБУДЬ СУКА КОММЕНТЫ НЕ ЗАБУДЬ СУКА
Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:
1)1 <= words.length <= 104
2)1 <= allowed.length <= 26
3)1 <= words[i].length <= 10
4)The characters in allowed are distinct.
5)words[i] and allowed contain only lowercase English letters.
"""

allowed1 = "ab"
words1 = ["ad", "bd", "aaab", "baa", "badab"]

allowed2 = "abc"
words2 = ["a", "b", "c", "ab", "ac", "bc", "abc"]

allowed3 = "cad"
words3 = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]


def countConsistentStrings(allowed, words):
    amount = 0
    bool_consistent = None
    for word in words:
        for symbol in word:
            if symbol not in allowed:
                bool_consistent = False
                break
            else:
                bool_consistent = True
        amount += bool_consistent
    return amount


print('First words:', words1)
print('Allowed symbols:', allowed1)
print('Amount of consistent strings:', countConsistentStrings(allowed1, words1), '\n')

print('Second words:', words2)
print('Allowed symbols:', allowed2)
print('Amount of consistent strings:', countConsistentStrings(allowed2, words2), '\n')

print('Third words:', words3)
print('Allowed symbols:', allowed3)
print('Amount of consistent strings:', countConsistentStrings(allowed3, words3))
