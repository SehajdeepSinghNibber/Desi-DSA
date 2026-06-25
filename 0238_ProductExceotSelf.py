def productExceptSelf(nums):
    resultList = []
    product = 1

    if 0 in nums:
        if nums.count(0) > 1:
            return [0] * len(nums)
        newList = [x for x in nums if x != 0]
        for i in range(len(newList)):
            product*=newList[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                resultList.append(product)
            else:
                resultList.append(0)
                
        return resultList
    else:
        for i in range(len(nums)):
            product*=nums[i]

    for i in range(len(nums)):
            newAddition = product//nums[i]
            resultList.append(newAddition)

    return resultList