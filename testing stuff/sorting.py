def bubble(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

print(bubble([7,56,4,23,32,56,78,89,7,45,3,2,34,56,6,8]))

def insertion(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] < temp:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst

print(insertion([7,56,4,23,32,56,78,89,7,45,3,2,34,56,6,8]))

def selection(lst):
    for i in range(len(lst)-1):
        max_inx = i
        for j in range(i+1, len(lst)):
            if lst[j] > lst[max_inx]:
                max_inx = j
        lst[i], lst[max_inx] = lst[max_inx], lst[i]
    return lst

print(selection([7,56,4,23,32,56,78,89,7,45,3,2,34,56,6,8]))