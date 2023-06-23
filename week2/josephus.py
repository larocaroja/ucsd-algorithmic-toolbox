def josephus(n, k):
    circle = list(range(n))
    current_idx = -1

    for _ in range(n-1):
        current_idx += k
        current_idx = current_idx%n
        circle.pop(current_idx)
        current_idx -= 1
        n -= 1

    return circle[0]

if __name__ == '__main__':
    n , k = map(int, input().split(' '))
    print(josephus(n, k))