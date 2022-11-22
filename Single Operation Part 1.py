# from math import log
from math import pow
for _ in range(int(input())):
    ln = int(input())
    stri = input()[:ln]
    count = 0
    for i in range(ln):
        if stri[i] == "1":
            count+=1
        elif stri[i] == "0":
            break
    print(count)
    
    # bina = int(input(),2)
    # # print(bina)
    # maxi = bina
    # maxy = 0
    # for y in range(1,bina+1):
    #     divi = pow(2,y)
    #     if divi<=bina:
    #         x = bina
    #         x = x^int(x/divi)
    #         if x > maxi:
    #             maxi = x
    #             maxy = y
    #     elif maxi == bina:
    #         maxy = y
    #         break
    #     else:
    #         break
    # print(maxy)
    # y = log((bina/-(~(bina))),2)
    # print(y)