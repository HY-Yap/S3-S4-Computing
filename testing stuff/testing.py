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

print('bubble sort:')
print(bubble([9,7,4,6,43,1,4,6,8,4,5,7,4,23,4,67,4,23,2]))

def insertion(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j >= 0 and lst[j] > temp:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst

print('insertion sort:')
print(insertion([9,7,4,6,43,1,4,6,8,4,5,7,4,23,4,67,4,23,2]))

def selection(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

print('selection sort:')
print(selection([9,7,4,6,43,1,4,6,8,4,5,7,4,23,4,67,4,23,2]))