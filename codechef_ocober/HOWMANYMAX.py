for _ in range(int(input())):
    l = int(input())
    b = [int(i) for i in input()]
    i = 0
    while i < len(b)-1:
        if b[i] == b[i+1]:
            b.pop(i)
            continue
        i+=1
    if b[0] == 1:
        if len(b)%2 == 0:
            print(int(len(b)/2)+1)
        else:
            print((len(b)//2)+1)
    if b[0] == 0:
        if len(b)%2 == 0:
            print(len(b)//2)
        else:
            print(len(b)//2 + 1)
    # print(b)