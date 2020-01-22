# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    print(elements); print("\n")

    index = 0; indexA = 0; indexB = 0
    while index != (elements):

        if arrA[indexA] <= arrB[indexB]:
            nextSmallest = arrA[indexA]; print(f"A smaller: {nextSmallest}")
            if indexA < len(arrA)-1:
                indexA += 1
            else:
                arrA[indexA] = float("inf")
        elif indexB != (len(arrB) - 1) :
            nextSmallest = arrB[indexB]; print(nextSmallest, indexB)
            if indexB < len(arrB)-1:
                indexB += 1

        merged_arr[index] = nextSmallest
        index += 1

    return merged_arr

array1 = [1, 4, 9, 11]
array2 = [2, 7, 23, 49, 99]
print(merge(array1, array2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
