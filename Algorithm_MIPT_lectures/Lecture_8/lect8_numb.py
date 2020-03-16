
def gen_bin(M, prefix=""):
    """Только для двоичной СС
    """
    if M==0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")



def generate_number(N:int, M:int, prefix=None):
    """Генерирует все числа(с лидирующими незначащими нулями)
    в N-ричной системе счисления (N<=10) длины М
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()

#Только для двоичной СС
gen_bin(2)

#Для произвольной СС
generate_number(2,2)


def find(number, A):
    """Ищет x в А и возвращает True если такой есть
    и False еси такого нет
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def generate_permutation(N:int, M:int=-1, prefix=None):
    """Генерация всех преестановок N чисел в M позицияхб
    с префиксом prefix
    """
    M = N if M == -1 else M  #по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=" ", sep="") # * как бы встраивает все значения(раскрывает массив)
        return
    for number in range(1, N+1):
        #нужно искулючить те числа что уже были
        if find(number, prefix):
            continue

        prefix.append(number)
        generate_permutation(N, M-1, prefix)
        prefix.pop()
print("\nВыводим перестановки")
generate_permutation(3)
