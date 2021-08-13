# This is the second approach to solve target_sum problem by using Hashmap aka dictionary in python

def pair_with_targetsum(arr, target_sum):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target_sum - num in nums:
      return [nums[target_sum - num], i]
    else:
      nums[arr[i]] = i
  return [-1, -1]


def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
