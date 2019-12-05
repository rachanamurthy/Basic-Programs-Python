class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenNeedle = len(needle)
        counter = 0
        if lenNeedle == 0:
            return 0
        for char in haystack:
            string = haystack[counter:counter+lenNeedle]
            if(string == needle):
                return counter
            counter = counter + 1
        return -1