def longestConsecutive(nums):
    if not nums:
        return 0

    nums.sort()
    returnList = [nums[0]]
    longest = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i]:
            continue
        elif nums[i + 1] == nums[i] + 1:
            returnList.append(nums[i + 1])
        else:
            longest = max(longest, len(returnList))
            returnList = [nums[i + 1]]

    return max(longest, len(returnList))