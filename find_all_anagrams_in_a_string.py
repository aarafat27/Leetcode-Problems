'''
problem link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize result list and frequency maps
        result = []
        p_freq = {}
        window_freq = {}

        # Initialize pointers for the sliding window
        start = 0
        end = 0

        # Initialize the frequency map for p
        for c in p:
            if c in p_freq:
                p_freq[c] += 1
            else:
                p_freq[c] = 1

        # Slide the window through the string s
        while end < len(s):
            # Add the current character to the window frequency map
            c = s[end]
            if c in window_freq:
                window_freq[c] += 1
            else:
                window_freq[c] = 1

            # If the window has the same size as p, check if the window is an anagram of p
            if end - start + 1 == len(p):
                # If the window is an anagram of p, add the start index to the result list
                if window_freq == p_freq:
                    result.append(start)

                # Remove the first character from the window and update the window frequency map
                d = s[start]
                window_freq[d] -= 1
                if window_freq[d] == 0:
                    del window_freq[d]
                start += 1

            end += 1

        return result
