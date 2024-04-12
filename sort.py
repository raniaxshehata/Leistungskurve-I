def bubble_sort(arr):
    n = len(arr)
    # durchläuft Array
    for i in range(n):
        # Letzte i Elemente -> bereits an der richtigen Stelle
        for j in range(0, n-i-1):
        # Element gefunden -> mit nächstgröperem Element tauschen
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Quelle: https://www.geeksforgeeks.org/python-program-for-bubble-sort/