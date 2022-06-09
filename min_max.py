def min_max(array,beg,end):
    global min,max
    if beg==end:
        min=max=array[0]
    elif end==beg+1:
        if array[beg]<array[end]:
            min=array[beg]
            max=array[end]
        else:
            min=array[end]
            max=array[beg]
    else:
        mid=(beg+end)//2
        min_max(array,0,mid)
        minl,maxl=min,max 
        min_max(array,mid+1,end)
        minr,maxr=min,max
        if minl<minr:
            min=minl
        else:
            min=minr
        if maxl>maxr:
            max=maxl
        else:
            max=maxr
array=[3,2,1,6,4,2,5,9,8,7]
beg=0
end=len(array)-1
min=0
max=0
min_max(array,0,end)
print(min,max)