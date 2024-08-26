# selection sort
def selection_sort(lst):
    for i in range(len(lst)-1):
        min_idx = i

        for j in range(i, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

print(selection_sort([73, 18, 45, 92, 6, 33, 87, 51, 29, 64, 12, 90, 37, 54, 81, 9, 42, 68, 23, 99, 76, 31, 7, 58, 84, 27, 66, 13, 49, 71, 85, 39, 93, 56, 22, 60, 74, 15, 52, 88, 34, 79, 5, 98, 20, 63, 44, 91, 26, 38, 11, 82, 70, 4, 67, 21, 57, 30, 89, 48, 95, 19, 77, 35, 83, 14, 55, 61, 2, 75, 24, 50, 97, 17, 43, 86, 3, 69, 32, 94, 62, 40, 8, 28, 53, 72, 16, 100, 78, 36, 10, 80, 41, 25, 59, 96, 1, 65, 47]))

# quick sort
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

print(quick_sort([73, 18, 45, 92, 6, 33, 87, 51, 29, 64, 12, 90, 37, 54, 81, 9, 42, 68, 23, 99, 76, 31, 7, 58, 84, 27, 66, 13, 49, 71, 85, 39, 93, 56, 22, 60, 74, 15, 52, 88, 34, 79, 5, 98, 20, 63, 44, 91, 26, 38, 11, 82, 70, 4, 67, 21, 57, 30, 89, 48, 95, 19, 77, 35, 83, 14, 55, 61, 2, 75, 24, 50, 97, 17, 43, 86, 3, 69, 32, 94, 62, 40, 8, 28, 53, 72, 16, 100, 78, 36, 10, 80, 41, 25, 59, 96, 1, 65, 47]))

# insertion sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        j = i - 1

        while j >= 0 and curr < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = curr
    return lst

print(insertion_sort([73, 18, 45, 92, 6, 33, 87, 51, 29, 64, 12, 90, 37, 54, 81, 9, 42, 68, 23, 99, 76, 31, 7, 58, 84, 27, 66, 13, 49, 71, 85, 39, 93, 56, 22, 60, 74, 15, 52, 88, 34, 79, 5, 98, 20, 63, 44, 91, 26, 38, 11, 82, 70, 4, 67, 21, 57, 30, 89, 48, 95, 19, 77, 35, 83, 14, 55, 61, 2, 75, 24, 50, 97, 17, 43, 86, 3, 69, 32, 94, 62, 40, 8, 28, 53, 72, 16, 100, 78, 36, 10, 80, 41, 25, 59, 96, 1, 65, 47]))

# bubble sort
def bubble_sort(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

print(bubble_sort([73, 18, 45, 92, 6, 33, 87, 51, 29, 64, 12, 90, 37, 54, 81, 9, 42, 68, 23, 99, 76, 31, 7, 58, 84, 27, 66, 13, 49, 71, 85, 39, 93, 56, 22, 60, 74, 15, 52, 88, 34, 79, 5, 98, 20, 63, 44, 91, 26, 38, 11, 82, 70, 4, 67, 21, 57, 30, 89, 48, 95, 19, 77, 35, 83, 14, 55, 61, 2, 75, 24, 50, 97, 17, 43, 86, 3, 69, 32, 94, 62, 40, 8, 28, 53, 72, 16, 100, 78, 36, 10, 80, 41, 25, 59, 96, 1, 65, 47]))

# merge sort
def merge(lst_a, lst_b):
    lst_c = []

    while len(lst_a) > 0 and len(lst_b) > 0:
        lst_c.append(lst_a.pop(0) if lst_a[0] < lst_b[0] else lst_b.pop(0))
    
    return lst_c + lst_a + lst_b

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        return merge(sorted_left, sorted_right)

print(merge_sort([73, 18, 45, 92, 6, 33, 87, 51, 29, 64, 12, 90, 37, 54, 81, 9, 42, 68, 23, 99, 76, 31, 7, 58, 84, 27, 66, 13, 49, 71, 85, 39, 93, 56, 22, 60, 74, 15, 52, 88, 34, 79, 5, 98, 20, 63, 44, 91, 26, 38, 11, 82, 70, 4, 67, 21, 57, 30, 89, 48, 95, 19, 77, 35, 83, 14, 55, 61, 2, 75, 24, 50, 97, 17, 43, 86, 3, 69, 32, 94, 62, 40, 8, 28, 53, 72, 16, 100, 78, 36, 10, 80, 41, 25, 59, 96, 1, 65, 47]))
