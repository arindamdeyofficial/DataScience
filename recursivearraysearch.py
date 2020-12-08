def arraysearch(arr, searchstartindex, key):
    if len(arr) < 1:
        print("Invalid Array")
        return
    if searchstartindex >= len(arr):
        return 'searchstartindex outside of array or item not found'
    if (arr[searchstartindex] == key):
        return str(key) + ' found at position ' + str(searchstartindex)
    #print(arr)
    return arraysearch(arr, searchstartindex+1, key)
