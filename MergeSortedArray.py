# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = 0
        second = 0
        cloneArr = nums1[:m]
        for i in range(m+n):
            if second>=n or (first<m and cloneArr[first] <= nums2[second]):
                nums1[i] = cloneArr[first]
                first+= 1
            else:
                nums1[i] = nums2[second]
                second+= 1
        return nums1

            
