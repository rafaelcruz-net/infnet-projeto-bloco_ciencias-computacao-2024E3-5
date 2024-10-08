def merge_sort(arr):
    if (len(arr) > 1):
        mid = len(arr) // 2
        
        L = arr[:mid]
        R = arr[mid:]

        # CHAMAMOS DE FORMA RECURSIVA O MERGE SORT, CASO PRECISE QUEBRAR MAIS SUBLISTA        
        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0

        # ORDENAMOS AS SUBLISTAS
        while i < len(L) and j < len(R):
            if (L[i] < R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        #JUNTAMOS A SUBLISTA A ESQUERDA
        while i < len(L): 
            arr[k] = L[i]
            i += 1
            k += 1
        
        #JUNTAMOS A SUBLISTA A DIREITA
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

arr = [38, 27, 43, 3, 9, 82, 10, 5, 8, 2]
print("Array original", arr)
print("Array ordenado com merge sort", merge_sort(arr))
            

