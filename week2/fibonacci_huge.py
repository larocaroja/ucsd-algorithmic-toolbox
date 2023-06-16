def fibonacci_huge(n, m):
    if n<=1:
        return n
    else:
        one_step_behind = 1
        two_step_behind = 0

        for i in range(1, n):
            value = one_step_behind + two_step_behind
            two_step_behind = one_step_behind % m
            one_step_behind = value % m
            value = value % m

    return value

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))