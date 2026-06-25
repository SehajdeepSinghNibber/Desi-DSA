class Solution(object):
    def reverse(self, x):
        # if x<0:
        #     x=-x
        #     x = str(x)[::-1]
        #     x = int(x)*-1
        # else:
        #     x = str(x)[::-1]
        #     x=int(x)

        # if x < -2**31 or x > 2**31 - 1:
        #     return 0

        # return x
    
    ## or

        rev = 0

        if x < -2**31 or x > 2**31 - 1:
                return 0

        if x < 0:
            x = -x
            sign = -1
        else:
            sign = 1

        while x:
            digit = x%10
            rev = rev*10+digit
            x = x//10


        return rev*sign