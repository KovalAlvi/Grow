def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left >1:
        middle = (left + right)//2
        if A[middle]<key:
            left = middle
        else:
            right = middle
    return left
A = [1,2,3,4,7,9]
print(A[left_bound(A, 3)])
