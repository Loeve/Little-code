def pascal_triangle(line):
    i, arr = 0, [1]
    for n in range(line):
        print(arr)
        arr = [1] + [arr[i] + arr[i+1] for i in range(0, len(arr) - 1)] + [1]
    return arr

pascal_triangle(10)
