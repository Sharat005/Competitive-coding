if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArr = sorted(arr, reverse=True)
    high = 0;
    secondHigh = 0;
    for idx, num in enumerate(newArr):
        if idx == 0:
            high = num
        elif num < high:
            secondHigh = num
            break;
    print(secondHigh);
        
