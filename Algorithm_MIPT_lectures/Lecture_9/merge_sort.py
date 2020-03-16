def merge(A, B):
    """Производит слияние двух отсортированных массивов
    Выводит массив длиной len(A)+len(B)
    """
    C = [0]*(len(A)+len(B))
    i=k=n=0
    while i<len(A) and k<len(B):
        if A[i] <= B[k]:
            C[n]=A[i]
            i+=1
            n+=1
        else:
            C[n]=B[k]
            n+=1
            k+=1
    while i<len(A):
        C[n] = A[i] ; i+=1 ; n+=1
    while k<len(B):
        C[n] = B[k] ; k+=1 ; n+=1

    return C

A = [1,20,18,6,8, 10]
B = [0, 3, 7,9,15]


def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i] = C[i]

print(*A)
merge_sort(A)
print(*A)
