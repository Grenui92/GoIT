def max_sequence(arr):
    max = 0
    max_list = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if sum(arr[i:j]) > max:
                max = sum(arr[i:j])
                max_list = arr[i:j]
    return max

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))