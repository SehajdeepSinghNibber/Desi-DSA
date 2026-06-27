class Solution:
    def merge(self, nums1, m, nums2, n):
        list3 = []

        for i in range(m):
            list3.append(nums1[i])

        for j in range(n):
            list3.append(nums2[j])

        p = len(list3)

        # for i in range(p):
        #     for j in range(p - i - 1):
        #         if list3[j] > list3[j + 1]:
        #             list3[j], list3[j + 1] = list3[j + 1], list3[j]

        list3.sort()

        for i in range(p):
            nums1[i] = list3[i]