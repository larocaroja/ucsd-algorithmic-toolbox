def fibonacci_partial_sum(m, n):
    cum_sum = 0
    
    current = 1
    previous = 0

    if n <= 1:
        return n

    for i in range(2, n+1):
        current, previous = (current + previous) % 10, current % 10

        if i >= m:
            cum_sum += current
            cum_sum = cum_sum % 10
            
    return cum_sum

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))