# Quick Sort — O(n log n) médio, O(n²) pior caso
# Implementado por: Letícia

trocas = 0

def quick_sort(arr):
    global trocas
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    trocas += len(arr)
    return quick_sort(left) + middle + quick_sort(right)
