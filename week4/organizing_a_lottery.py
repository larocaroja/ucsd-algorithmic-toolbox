def organize_a_lottery(seq, l, r, p):
    if r-l<1:
        if (seq[l][0] <= p) and (p <= seq[l][1]):
            return 1
        else:
            return 0
    
    m = l + (r-l)//2
    start_m, end_m = seq[m]

    if start_m > p:
        return organize_a_lottery(seq, l, m, p)
    
    elif end_m >= p:
        return organize_a_lottery(seq, l, m, p) + organize_a_lottery(seq, m+1, r, p)
    
    else:
        return organize_a_lottery(seq, l, m, p) + organize_a_lottery(seq, m+1, r, p)


if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    
    seq =[]
    for _ in range(n):
        seq.append(list(map(int, input().split(' '))))

    seq = sorted(seq, key = lambda x: x[1])
    p = list(map(int, input().split(' ')))

    for i, p_ in enumerate(p):
        if i != m-1:
            print(organize_a_lottery(seq, 0, n-1, p_), end = ' ')
        else:
            print(organize_a_lottery(seq, 0, n-1, p_))