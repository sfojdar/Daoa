def quick_sort(arr, beg, end):
    if(beg < end):
        pivotIndex = partition(arr, beg, end)
        quick_sort(arr, beg, pivotIndex)
        quick_sort(arr, pivotIndex+1, end)
def partition(arr, beg, end):
    pivot = arr[beg]
    p = beg+1
    q = end
    while True:
        while(p <= q and arr[p] <= pivot):
            p = p+1
        while(p <= q and arr[q] >= pivot):
            q = q-1
        if(p <= q):
            arr[p], arr[q] = arr[q], arr[p]
        else:
            arr[beg], arr[q] = arr[q], arr[beg]
            return q
arr = [44, 33, 11, 55, 77, 90, 40, 60, 99, 22, 88]
print('Unsorted array:', arr)
quick_sort(arr, 0, 10)
print('Sorted array', arr, '\n')