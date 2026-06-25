class Solution(object):
    def maxSubArray(self, nums):

        result = nums[0]
        finalResult = nums[0]

        for i in range(1,len(nums)):
            if result+ nums[i] >= result:
                result = result+nums[i]
            else:
                result = nums[i]
            finalResult = max(result,finalResult)

        return finalResult