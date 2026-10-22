class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t1 = t[:]
        for i in range(len(s) - 1):
            if s[i] not in t1:
                return False
            else:
                t1 = t1.replace(s[i], "", 1)
        
        if s[-1] == t1:
            return True
        else:
            return False

