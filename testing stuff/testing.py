def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0 and lst[j] > lst[i]:
            j -= 1
        lst.insert(j+1, lst.pop(i))
    return lst

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def imprv_bubble_sort(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def merge(lst_a, lst_b):
    lst_c = []
    while len(lst_a) > 0 and len(lst_b) > 0:
        lst_c.append(lst_a.pop(0) if lst_a[0] < lst_b[0] else lst_b.pop(0))
    return lst_c + lst_a + lst_b

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        return merge(sorted_left, sorted_right)

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left, right = [], []

        for item in lst[1:]:
            if item <= pivot:
                left.append(item)
            else:
                right.append(item)
        
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return sorted_left + [pivot] + sorted_right

lst = [0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,0]
print(insertion_sort(lst))
print(selection_sort(lst))
print(imprv_bubble_sort(lst))
print(merge_sort(lst))
print(quick_sort(lst))