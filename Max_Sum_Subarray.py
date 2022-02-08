def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  Sum = 0
  maxSum = 0
  i = 0

  for j in range(len(arr)):
    if(j > k-1):
      Sum -= arr[i]
      i += 1
      
    Sum += arr[j]
    maxSum = max(maxSum, Sum)


  return maxSum
