from matplotlib.pyplot import flag


for _ in range(int(input())):
    ln = int(input())
    stri = input()[:ln]
    count = 1
    for i in range(1,ln):
        if stri[i]=="1":
            break
        else:
            count+=1
    print(count)