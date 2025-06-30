# 4 + 4 + 4 + 4 + 3 + 8 + 8

cits = list(map(int, input().split()))

cits.sort(reverse=True)
h_index = 0
for i, val in enumerate(cits, 1):
    if val >= i:
        h_index = i
    else:
        break
print(h_index)