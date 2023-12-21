'''
problem link: https://leetcode.com/problems/word-pattern/
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        mapping = {}
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            if letter in mapping:
                if mapping[letter] != word:
                    return False
            else:
                if word in mapping.values():
                    return False
                mapping[letter] = word
        return True
