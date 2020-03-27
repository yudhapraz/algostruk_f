##def swap (A, p, q):
##    tmp = A[p]
##    A[p] = A[q]
##    A[q] = tmp
##    
##def cariPosisiTerkecil(A, dariSini, sampaiSini):
##    posisiTerkecil = dariSini
##    for i in range(dariSini+1, sampaiSini):
##       if A[i] < A[posisiTerkecil]:
##            posisiTerkecil = i
##    return posisiTerkecil
##A = [18, 13, 44, 25, 66, 107, 78, 89]
##
##j = cariPosisiTerkecil(A, 2, len(A))

##L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
##def bubbleSort(A):
##   n = len(A)
##   for i in range(n-1):
##        for j in range(n-i-1):
##            if A[j] > A[j+1]:
##                swap(A, j, j+1)
##bubbleSort(L)
##


##L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
##def selectionSort(A):
##    n = len(A)
##    for i in range(n-1):
##       indexKecil = cariPosisiTerkecil(A, i, n)
##       if indexKecil != i:
##            swap(A, i, indexKecil)
##selectionSort(L)

L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos -1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
insertionSort(L)

