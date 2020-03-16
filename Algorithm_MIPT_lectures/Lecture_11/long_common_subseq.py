import matplotlib.pyplot as plt


A = [i for i in range(10)]
B = [j for j in range(0,20,2)]



def lcs(A:list, B:list):
    """
    Находит наибольшую общую подпоследовательность
    Выводит её длину и саму последовательность
    """
    print(A,"\n", B)
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    sub = []
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
                sub.append(A[i-1])
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    plt.imshow(F)
    plt.show()
    return F[-1][-1], sub

print(lcs(A, B))
