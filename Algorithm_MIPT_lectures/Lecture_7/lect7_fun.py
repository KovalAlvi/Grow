# Вычисление фрактала
def fact(n:int):
    assert n>=0, "Факториал отрицательного числа не определен"
    if n == 0:
        return 1
    return fact(n-1)*n

#print(fact(4))


#Алгоритмы по вычислению НОД
def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        return(gcd(a-b,b))
    else: #a<b
        return gcd(a, b-a)

def gcd_1(a, b):
    if b==0:
        return a
    else:
        return gcd_1(b, a%b)

def gcd_2(a, b):
    """Тоже самое что и предыдущее
    ТОлько в одну строчку"""
    return (a if b==0 else gcd_2(b, a%b))




def pow(a, n):
    if n==0:
        return 1
    else:
        return pow(a, n-1)*a

def fast_pow(a, n):
    if n==0:
        return 1
    elif n%2==1:
        return fast_pow(a, n-1)*a
    else:
        return fast_pow(a**2, n//2)

if __name__=='__main__':
    from timeit import Timer
    t = Timer("pow(2,100)", "from __main__ import pow")
    print(t.timeit())
    t_2 = Timer("fast_pow(2,100)", "from __main__ import fast_pow")
    print(t_2.timeit())
