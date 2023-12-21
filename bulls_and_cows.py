'''
problem link: https://leetcode.com/problems/bulls-and-cows/
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        guess_map = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in guess_map:
                    guess_map[secret[i]] += 1
                else:
                    guess_map[secret[i]] = 1
        
        for i in range(len(guess)):
            if secret[i] != guess[i] and guess[i] in guess_map and guess_map[guess[i]] > 0:
                cows += 1
                guess_map[guess[i]] -= 1
        
        return f"{bulls}A{cows}B"
