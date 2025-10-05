def bubble(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

# print(bubble([16,4,3,43,4,87,9,578,645,354,4,43,3,1]))

def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    return c + a + b

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        sorted_l = merge_sort(l)
        sorted_r = merge_sort(r)
        return merge(sorted_l, sorted_r)

# print(merge_sort([16,4,3,43,4,87,9,578,645,354,4,43,3,1]))

def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left, right = [], []

        for ele in arr[1:]:
            left.append(ele) if ele < pivot else right.append(ele)
        
        sorted_left = quick(left)
        sorted_right = quick(right)

        return sorted_left + [pivot] + sorted_right

# print(quick([16,4,3,43,4,87,9,578,645,354,4,43,3,1]))

def binary_search(arr, itm):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if itm == arr[mid]:
            return mid
        elif itm < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15, 16]
print(binary_search(lst, 13))  # 13