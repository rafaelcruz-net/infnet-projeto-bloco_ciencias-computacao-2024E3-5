def bubble_sort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 50, 55, 90, 10, 9, 7, 1]
print("Array original: ", arr)
print("Array ordenado com bubble sort: ", bubble_sort(arr))

