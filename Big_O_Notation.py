#Big o notation is a way to measure the efficiency of an algorithm. It is a way to describe how the runtime of an algorithm grows as the input
#size grows.

A = [5, 2, 4, 6, 1, 3]


for j in range(1 , len(A)):
    key = A[j]
    # Insert A[j] into the sorted sequence A[1..j-1].
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

print("Arreglo A ordenado: ", A)