class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = []
        finalResult = 0

        for i in range(len(s)):
            if s[i] not in result:
                result.append(s[i])
            else:
                id = result.index(s[i])
                result = result[id+1:]
                result.append(s[i])
        
            finalResult = max(len(result),finalResult)

        return finalResult