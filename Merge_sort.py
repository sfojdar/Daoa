def mergesort(arr):
    if len(arr)>1:
        left_array=arr[:len(arr)//2]
        right_array=arr[len(arr)//2:]
        mergesort(left_array)
        mergesort(right_array)
        i=0
        j=0
        sorted_array=[]
        while i <len(left_array) and j<len(right_array):
            if left_array[i]<right_array[j]:
                sorted_array.append(left_array[i])
                i=i+1
            else:
                sorted_array.append(right_array[j])
                j=j+1
        while i<len(left_array):
            sorted_array.append(left_array[i])
            i=i+1
        while j<len(right_array):
            sorted_array.append(right_array[j])
            j=j+1
        print(sorted_array)
arr=[45,26,21,18,5,9,16,34]
mergesort(arr)