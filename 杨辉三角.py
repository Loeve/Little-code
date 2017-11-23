#不用生成器
def pascal_triangle(line):
    i, arr = 0, [1]
    for n in range(line):
        print(arr)
        arr = [1] + [arr[i] + arr[i+1] for i in range(0, len(arr) - 1)] + [1]
    return arr

pascal_triangle(10)

#生成器
def pascal_triangle(line):
    i, arr = 0, [1]
    for n in range(line):
        yield (arr)
        arr = [1] + [arr[i] + arr[i+1] for i in range(0, len(arr) - 1)] + [1]
    return 'over'
#测试
g = pascal_triangle(10)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value", e.value)
        break
