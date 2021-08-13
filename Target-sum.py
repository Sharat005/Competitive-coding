# https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP

# this one uses a two pointer approach and pattern

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  front = 0;
  back = len(arr)-1;

  for i in range(len(arr)):
    sum = arr[front]+arr[back];
    if(sum<target_sum):
      front = front + 1;
    elif(sum>target_sum):
      back-= 1;
    else:
      return [front, back];
