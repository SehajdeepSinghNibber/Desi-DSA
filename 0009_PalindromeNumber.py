class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False
        
        x = str(x)

        if x == x[::-1]:
            return True
        
        return False
        
        # or

        # x = str(x)

        # for i in range(0,len(x)//2):
        #     if x[i] != x[len(x)-i-1]:
        #         return False
        # return True