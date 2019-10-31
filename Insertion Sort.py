

li=[7,8,1,23,4,5]

def insertion_sort(li):
    j=1
    for i in range(1,len(li)):###ggoing from the 1st element to the end
        j=i-1
        key=li[i]
        while j>=0 and li[j]>key:##j till we find where to put the ith element
            li[j+1]=li[j]####move the elemnts one step ahead  eg: jj=1  then li[2]=li[1] becomes==[7,8,8] then j=0 then li[1]=li[0] ==[7,7,8]  yhen li[0]=keyy
            j-=1
        li[j+1]=key
insertion_sort(li)
