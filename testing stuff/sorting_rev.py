def bs(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

# print(bs([54,96,2356,124,58,70,6345,245,68,3,8,5,4,2,0,6475,24]))

def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    return c + a + b

def ms(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        l = lst[:mid]
        r = lst[mid:]

        sl = ms(l)
        sr = ms(r)

        return merge(sl, sr)

# print(ms([54,96,2356,124,58,70,6345,245,68,3,8,5,4,2,0,6475,24]))

def qs(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        l, r = [], []
        for itm in lst[1:]:
            l.append(itm) if itm < pivot else r.append(itm)
        
        sl = qs(l)
        sr = qs(r)

        return sl + [pivot] + sr

# print(qs([54,96,2356,124,58,70,6345,245,68,3,8,5,4,2,0,6475,24]))

def bin(lst, ele):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if ele == lst[mid]:
            return mid
        else:
            if ele < lst[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1

print(bin([1,2,3,4,5,6,7,8,9,10], 8))