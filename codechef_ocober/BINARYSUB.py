for _ in range(int(input())):
    stri = input()
    lenab = 0
    lenba = 0
    for i in range(len(stri)-1):
        if stri[i] == "a" and stri[i+1] == "b": 
            lenab += 1
        if stri[i] == "b" and stri[i+1] == "a":
            lenba += 1
    sum = pow(2,lenab+lenba)
    print(sum)

