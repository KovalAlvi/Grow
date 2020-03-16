

def traj_num(N):
    """Ищет количество возможных траекторий по достижению
    цели. Кузнечик может прыгать на +1 и +2
    Сколько траекторий по достижению N клетки
    """
    k = [0,1] + [0]*(N-1)
    for i in range(2,N+1):
        k[i] = k[i-2]+k[i-1]
    return k[N]

print(traj_num(1))

#Теперь случай, когда запрещают во что-то наступать
N = 20
allowed = [True]*N
allowed[7] = allowed[10] =  False

def count_traj(N, allowed:list):
    """Считает тоже самое только за исключением некоторых точек
    """
    k = [0,1,allowed[2]] + [0]*N-3
    for i in range(3,N+1):
        if allowed[i]:
            k[i] = k[i-1] + k[i-2] + k[i-3]
