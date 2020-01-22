
def switch(smallest_index, i, arr):
    temp = arr[smallest_index]
    arr[smallest_index] = arr[i]
    arr[i] = temp
    return arr

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr) - 1):
            if arr[smallest_index] > arr[j+1]:
                smallest_index = j+1

        # TO-DO: swap
        if i != smallest_index:
            # temp = arr[smallest_index]
            # arr[smallest_index] = arr[i]
            # arr[i] = temp
            arr = switch(smallest_index, i, arr)
        
    return arr
testArray = [4, 3, 1, 2, 6, 5]
print(selection_sort(testArray))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    notDone = True
    while notDone:
        # loop thru entire array even tho you should loop thru one less index each time
        notDone = False
        for index in range(0, len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr = switch(index + 1, index, arr)
                notDone = True
    return arr


testArray2 = [2, 3, 1, 4, 6, 5, 9, 7, 8, 10]
print(bubble_sort(testArray2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr