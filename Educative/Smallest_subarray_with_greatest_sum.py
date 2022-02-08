def smallest_subarray_sum(s, arr):
  # TODO: Write your code here
  output = float('inf')
  Sum = 0
  i = 0

  for j in range(len(arr)):
    Sum += arr[j]

    while Sum >= s:
      output = min(output, j-i+1)
      Sum -= arr[i]
      i += 1
    
    


  return output
