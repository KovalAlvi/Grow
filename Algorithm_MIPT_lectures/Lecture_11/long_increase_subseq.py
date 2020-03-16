def lis(A):
    """
    Выводит длину наибольшей возрастающей подпоследовательности
    """
    F = [0]*(len(A)+1) # считает длину НВП
    sub = []
    for i in range(1, len(A)+1):
        m = 0
        sub.append(A[i])
        for j in range(0,i):
            if A[i-1] >A[j-1] and F[j] >m:
                m = F[j]
                sub.append(A[i])
        sub.pop()

        F[i] = m+1


    return F[-1], sub

A= [1,3,45,6,7,81]
print(lis(A))
