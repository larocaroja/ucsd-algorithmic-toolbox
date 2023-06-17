def fibonacci_partial_sum(m, n):
    assert m>=0 and m<=n, 'm is out out of range'
    assert n>=m and n<=10**14, 'n is out out of range'

    fib_seq = [0, 1, 1]
    p = 2

    is_repeated = (fib_seq[p] == 1 and (fib_seq[p-1] == 0))
    is_end = (p == n)

    if n <= 2:
        return sum(fib_seq[m:n+1])
    
    while (not is_repeated) and (not is_end):
        fib_number = (fib_seq[p] + fib_seq[p-1]) % 10
        fib_seq.append(fib_number)

        p += 1
        is_repeated = (fib_seq[p] == 1 and (fib_seq[p-1] == 0))
        is_end = (p == n)

    if is_repeated:
        fib_seq = fib_seq[:-2]
        repetition, m_, n_  = (n-m+1) // (p-1), m % (p-1), n % (p-1)
        cum_sum = (sum(fib_seq) * repetition + sum(fib_seq[m_:]) + sum(fib_seq[:n_+1])) % 10
    elif is_end:
        cum_sum = sum(fib_seq[m:n+1]) % 10
    
    return cum_sum

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))