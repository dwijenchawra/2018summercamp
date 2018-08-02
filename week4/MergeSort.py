def mergeSortTimeTrail(arr):
    #timein
    mergeSort(arr)
    #timeout

def mergeSort(arr):

    if len(arr) == 1:
        return arr
    else:
        """print(len(arr)/2)
        print("first half: "+str(arr[0:int(len(arr)/2)]))
        print("second half: "+str(arr[int(len(arr)/2):]))

        merged = callMerge(mergeSort(arr[0:int(len(arr)/2)]), mergeSort(arr[int(len(arr)/2):]))
        print("combined: " +str(merged))"""
        return callMerge(mergeSort(arr[0:int(len(arr)/2)]), mergeSort(arr[int(len(arr)/2):]))

def callMerge(arr1,arr2):
    temp = []
    return merge2(arr1,arr2,temp)
def merge2(arr1,arr2,arrRet):
    if len(arr1) == 0:
        for i in range(len(arr2)):
            arrRet.append(arr2[i])
        return arrRet
    elif len(arr2) == 0:
        for i in range(len(arr1)):
            arrRet.append(arr1[i])
        return arrRet
    else:
        if arr1[0]<arr2[0]:
            arrRet.append(arr1[0])
            return merge2(arr1[1:],arr2,arrRet)
        else:
            arrRet.append(arr2[0])
            return merge2(arr1,arr2[1:],arrRet)

def merge_call(list1, list2):
    newlist = []
    return merge(list1, list2, newlist)

def merge(list1, list2, newlist):
    if len(list1) and len(list2) == 0:
        return newlist
    elif len(list1) == 0:
        newlist.append(list2)
        return newlist
    elif len(list2) == 0:
        newlist.append(list1)
        return newlist
    elif len(list1) >= len(list2):
        length = len(list1)
    else:
        length = len(list2)
    if length > 0:
        if list1[0] >= list2[0]:
            newlist.append(list1[0])
            list1.pop(0)
    else:
        return newlist
print(mergeSort([5,334,234,623,12,52,62,23, 62,76,954,23,52,23,12,15]))
