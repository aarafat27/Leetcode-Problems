'''
problem link: https://leetcode.com/problems/longest-repeating-character-replacement/
'''
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        char_counts = Counter()
        for right in range(len(s)):
            char_counts[s[right]] += 1
            max_char_count = char_counts.most_common(1)[0][1]
            while right - left + 1 - max_char_count > k:
                char_counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
