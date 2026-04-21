def nonRecursiveBynarySearch(list, target):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (high + low) // 2
        found = list[mid]
        if found == target:
            return mid
        
        if found > target:
            high = mid - 1

        if found < target:
            low = mid + 1
        
    return None
    

list = [1,3,5,7,9,10]
target = 7
#print (nonRecursiveBynarySearch(list, target))

#if function is within a class it needs self argument, if not, doesn't

def recursiveBynarySearch(list, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        found = list[mid]
        if found == target:
            return mid
        if found < target:
            return recursiveBynarySearch(list, target, mid+1, high)

        if found > target: 
            return recursiveBynarySearch(list, target, low, mid-1)    
    else:
        return None


list = [1,3,5,7,9,10,11]
target = 1
low = 0
high = len(list)-1
print(recursiveBynarySearch(list, target, low, high))