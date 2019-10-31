li=[7,8,345,121,4,7,3231212314,324,457,34,1,23,4,5]

def selection_sort(li):
    unsorted=-1
    for i in range(len(li)):
        minim=min(li[unsorted+1:])
        minim_index=[i for i in range(unsorted+1,len(li)) if li[i]==minim][0]
        temp=li[minim_index]
        li[minim_index]=li[unsorted+1]
        li[unsorted+1]=temp
        unsorted+=1
    print(li)



selection_sort(li)
