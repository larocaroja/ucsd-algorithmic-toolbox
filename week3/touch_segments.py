def touch_segments_recursive(seq):
    if len(seq) == 0:
        return 0
    
    if len(seq) == 1:
        return 1
    
    _, r = seq[0]
    seq.pop(0)

    for _, (l_, r_) in enumerate(seq):
        if r < l_:
            break
        elif l_ <= r and r <= r_:
            seq.remove([l_, r_])
    
    return 1 + touch_segments_recursive(seq)

def touch_segments_iterative(seq):
    n_points = 0
    points = []
    last_point = 0

    for i, (l_, r_) in enumerate(seq):
        if (i != 0) and (last_point >= l_) and (last_point <= r_):
            continue

        points.append(str(r_))
        n_points += 1
        last_point = r_

    return n_points, points


if __name__ == '__main__':
    n = int(input())
    seq = []
    for _ in range(n):
        l, r = map(int, input().split(' '))
        seq.append([l,r])

    seq = sorted(seq, key = lambda x: x[1])


    n_points, points = touch_segments_iterative(seq)
    print(n_points)
    print(' '.join(points))