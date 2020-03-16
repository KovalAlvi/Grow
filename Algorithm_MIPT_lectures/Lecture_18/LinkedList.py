

class LinkedList:
    """Создание одновязного списка с добавлением в начало нового элемента
    и с доставанием верхнего элемента первого элемента"""
    def __init__(self):
        self._begin =  None
    def incert(self, x): #Добавление в начало списка
        self._begin= [x, self._begin]

    def pop(self):
        assert self._begin is not None, "Is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


A = LinkedList()

print(A._begin)
A.incert(10)

print(A._begin)
A.incert(20)

print(A._begin)
