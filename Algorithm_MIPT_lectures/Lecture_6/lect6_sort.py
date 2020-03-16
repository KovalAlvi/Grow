
def incert_sort(A):
    """Сортировка списка A вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]: #ленивый оператор И если первое ложное, то он не станет определять второе выражение
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """Cортировка списка А выбором"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """Сортировка списка A методом пузырька"""
    N = len(A)
    #проходы bypass
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_algorith):
    print("Тестируем:", sort_algorith.__doc__ )
    print("testcace #1:", end="")
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algorith(A)
    print("Ok" if A==A_sorted else "Fail")

    print("testcace #2:", end="")
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorith(A)
    print("Ok" if A==A_sorted else "Fail")

    print("testcace #3:", end="")
    A = [4,2,4,2,1]
    A_sorted = [1,2,2,4,4]
    sort_algorith(A)
    print("Ok" if A==A_sorted else "Fail")

if __name__ == "__main__":
# Выполнение идет только в том случае, если мы вызываем этот файл напрямую,
#А не привязываем к другой программе, как библиотеку
    test_sort(incert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
