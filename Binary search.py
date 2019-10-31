x=list(map(int,input().split()))

x.sort()

def binarySearch(x,item):
    min_x=0
    flag=0
    max_X=len(x)
    for i in range(0,len(x)):
        mid=(min_x+max_X)//2
        if x[mid]==item:
            flag=1
            print("found at the "+str(mid+1)+"position")
            break
        elif x[mid]>item:
            max_X=mid-1
        else:
            min_x=mid+1
    if flag == 0:
        print("not found at any position")



binarySearch(x,2)


