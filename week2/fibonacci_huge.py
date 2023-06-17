def fibonacci_huge(n, m):
    assert n>=1 and n<=10**14, 'n is out out of range'
    assert m>=2 and m<=10**3, 'm is out out of range'

    fib_seq = [0, 1, 1]
    idx = p = 2

    is_repeated = (fib_seq[p] == 1 and (fib_seq[p-1] == 0))
    is_end = (p == n)

    if n == 1:
        return n
    
    while (not is_repeated) and (not is_end):
        fib_number = (fib_seq[p] + fib_seq[p-1]) % m
        fib_seq.append(fib_number)

        p += 1
        is_repeated = (fib_seq[p] == 1 and (fib_seq[p-1] == 0))
        is_end = (p == n)

    if is_repeated:
        idx = n % (p-1)
    elif is_end:
        idx = p
    
    return fib_seq[idx]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))