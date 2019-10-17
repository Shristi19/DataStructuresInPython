import math
def function(l):
    floor_value=math.floor(len(l)/2);
    set_unique=set(l)
    hash={}
    for i in set_unique:
        hash[i]=l.count(i)
    x=max(hash,key=hash.get)
    value_max=hash[x]
    if value_max >=floor_value:
        print(max(hash,key=hash.get))
    else:
        print("Not found")










ins=list(map(int,input().split()))

function(ins)

#####to get max values in a dict from a dict value:------max(dictionary,key=dictionary.get) .get is for values
