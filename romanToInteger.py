# 13. Roman to Integer(LeetCode)
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for char in range(len(s)):
            if char+1!=len(s) and romans[s[char]]<romans[s[char+1]]:
                result = result - romans[s[char]]
            else:
                result = result+romans[s[char]]
        return result