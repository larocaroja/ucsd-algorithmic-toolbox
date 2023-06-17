def fibonacci_sum_square_last_digit(n):
    assert n>=0 and n<=10**14, 'n is out out of range'

    fib_seq = [0, 1, 1]
    p = 2

    is_repeated = (fib_seq[p] == 1 and (fib_seq[p-1] == 0))
    is_end = (p == n)

    if n <= 2:
        return sum([v**2 for v in fib_seq[:(n+1)]])
    
    while (not is_repeated) and (not is_end):
        fib_number = (fib_seq[p] + fib_seq[p-1]) % 10
        fib_seq.append(fib_number)

        p += 1
        is_repeated = (fib_seq[p] == 1 and (fib_seq[p-1] == 0))
        is_end = (p == n)

    if is_repeated:
        fib_seq = fib_seq[:-2]
        # quotient, remainder = n//(p-1), n%(p-1)
        idx = n % (p-1)
    elif is_end:
        idx = n

    cum_sum = (fib_seq[idx] * (fib_seq[idx] + fib_seq[idx-1])) % 10

    return cum_sum

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_square_last_digit(n))