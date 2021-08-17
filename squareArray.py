# https://www.educative.io/courses/grokking-the-coding-interview/R1ppNG3nV9R

# This is very simple using python

# My own method in leetcode

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums);
        startPtr = 0;
        endPtr = n-1;
        squares = [0] * n;
        for i in range(len(nums)-1, -1, -1):
            if(nums[startPtr]*nums[startPtr]>nums[endPtr]*nums[endPtr]):
                squares[i] = nums[startPtr]*nums[startPtr]
                startPtr+=1;
            else:
                squares[i] = nums[endPtr]*nums[endPtr]
                endPtr-=1
        return squares;
        
# educative method

def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
