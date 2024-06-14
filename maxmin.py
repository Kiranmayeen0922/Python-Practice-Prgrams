#max and min value in an array

def minmax(arr):
    if not arr: 
        return None, None
    minelem=arr[0]
    maxelem=arr[0]
    for num in arr[1:]:
        if num<minelem:
            minelem=num
        if num>maxelem:
            maxelem=num
    return minelem, maxelem
array = [1000,20000,60000,40000,900]
minelement, maxelement = minmax(array)
print(f" minimum element is {minelement}")
print(f" maximum element is {maxelement}")