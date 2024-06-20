# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    compl_nums = nums1 + nums2
    compl_nums.sort()
    long = len(compl_nums)
    if long % 2 == 0:
        median = int(long / 2)
        new_list = compl_nums[(median - 1):(median + 1)]
        result = sum(new_list) / 2
    else:
        median = int(long // 2)
        result = float(compl_nums[median])
    return result

