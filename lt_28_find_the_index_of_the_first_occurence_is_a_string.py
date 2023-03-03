'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        l, n, r = 0, 0, 0

        while r < len(haystack):
            while r < len(haystack) and haystack[r] == needle[n]:
                r += 1
                n += 1
                if n == len(needle):
                    return l
            n = 0
            l += 1
            r = l
        
        return -1
    
        # return haystack.find(needle)

# Time O(H + N), Space O(1)

