from collections import Counter
class Solution:
    def solve(self, s):
        counter = Counter(s)
        found = False
        
        for letter in counter:
            if counter[letter] % 2 != 0:
                if not found:
                    found = True
                else:
                    return False
        
        return True
