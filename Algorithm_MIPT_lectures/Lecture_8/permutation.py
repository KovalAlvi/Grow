
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
