def check_sorted(A, ascending = True):
    """Проверка отсортированности за О(len(A))
    (ascendin по возрастанию или нет)
    """
    flag = True
    s = 2*int(ascending)-1
    N = len(A)
    for i in range(0, N-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag
A = [1,2,3,4,5,5,5,0]
print(check_sorted(A))
