# https://www.educative.io/courses/grokking-the-coding-interview/mEEA22L5mNA

# This is my own method using two pointer approach in a single loop
# The another method specified online is finding non-duplicates in an array and replacing the array row wise so that first n numbers will be all non-duplicates which can be counted

def remove_duplicates(arr):
  # TODO: Write your code here
  firstPtr = 0
  secondPtr = 1
  count = 1;
  for i in range(1,len(arr)):
    if(arr[firstPtr]==arr[secondPtr]):
      secondPtr = i + 1;
    else:
      count+=1;
      secondPtr = i + 1;
      firstPtr = i;
  return count;

# Second method

def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
