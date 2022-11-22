from math import ceil


for _ in range(int(input())):
    n,x = map(int,input().split())
    result = ceil(n*x / 4)
    print(result)