# https://leetcode.com/problems/find-peak-element/submissions/

# Brute force is to just do a linear scan on loop and check if a[i]>a[i+1]

def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
