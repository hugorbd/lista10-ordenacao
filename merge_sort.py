# Merge Sort — O(n log n) no pior caso
# Implementado por: Hugo

movimentos = 0

def merge_sort(arr):
    global movimentos
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
        movimentos += 1
    result.extend(left[i:])
    result.extend(right[j:])
    movimentos += len(left[i:]) + len(right[j:])
    return result