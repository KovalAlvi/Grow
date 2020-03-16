def hoar_sort(A):
    if len(A)<=1:
        return
    barrier = A[0]
    L = []; M = []; R = []
    for x in A:
        if x<barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
A = [1,2,34,5]
B = [-1,3,4,5,4]
hoar_sort(B)
print(B)