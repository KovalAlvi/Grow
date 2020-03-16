

def find_prefix(A):
    """Выводит максимальную длину префикса
    равного суффиксу для списка"""

    P = [0]*len(A)
    for i in range(1,len(A)):
        p = P[i-1]
        while p > 0 and A[i] != A[p]: #происходит углубление(рукурсивно)
            p = P[p-1]
        if A[i] == A[p]: #Захватываем нужный символ и расширяемся
            p = p + 1
        P[i] = p
    return P[-1]


if __name__ == "__main__":
    A = "abahgfyrklsjhvdcjhfdkaba"
    print(A, find_prefix(A))
