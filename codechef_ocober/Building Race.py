for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    chefs = a/x
    chefis = b/y
    if chefs<chefis:
        print("Chef")
    elif chefs>chefis:
        print("Chefina")
    else :
        print("Both")