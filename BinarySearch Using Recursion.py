
x=list(map(int,input().split()))
x.sort()

def binarySearchUsingRecursion(x,item,min_x,max_X):
    flag=0
    for i in range(0,len(x)):
        mid=(min_x+max_X)//2
        if x[mid]==item:
            flag=1
            return print("found at the "+str(mid+1)+"position")
        elif x[mid]>item:
            max_X=mid-1
            return binarySearchUsingRecursion(x,item,min_x,max_X)
        else:
            min_x=mid+1
            return binarySearchUsingRecursion(x,item,min_x,max_X)

    if flag == 0:
        print("not found at any position")



binarySearchUsingRecursion(x,2,0,len(x))


