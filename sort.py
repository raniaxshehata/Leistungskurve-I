def bubble_sort(arr):
    n = len(arr)
    # Durchlaufe das Array
    for i in range(n):
        # Letzte i Elemente sind bereits an der richtigen Stelle
        for j in range(0, n-i-1):
            # Tausche, wenn das Element gefunden wird, das größer als das nächste Element ist
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
