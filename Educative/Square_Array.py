def make_squares(arr):
  squares = [0] * len(arr)
  start = 0
  n = len(arr)
  end = n - 1
  i = n - 1
  while(start != end):
    if (arr[start]**2) > (arr[end]**2):
      squares[i] = arr[start]**2
      start += 1
    else:
      squares[i] = arr[end]**2
      end -= 1
    i -= 1
     

  return squares
