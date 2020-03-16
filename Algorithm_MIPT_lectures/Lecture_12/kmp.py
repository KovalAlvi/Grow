import prefix as my



def kmp(A, sub):
    """Ищет подстроки в строке и выводит массив
    начало подстроки в заданной строке
    Асимптотика поиска O(N+M)
    Намного быстрее обычного перебора"""
    A_new = sub+'#'+A
    index = []
    for i in range(len(A_new)):
        if my.find_prefix(A_new[:i+1]) == len(sub):
            num = i - 2*len(sub)
            index.append(num)
    return index

if __name__ == "__main__":
    A = "asdddadsfasfsdasdfasdaasfgafsgsd5q"
    sub = "q"

    index = kmp(A, sub)
    print(A)
    for num in index:
        print(A[num:num+len(sub)], num)
