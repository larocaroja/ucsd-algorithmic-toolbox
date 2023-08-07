import random

def count_inversion(seq, l, r):
    def merge(p,q):
        ret = []
        n_inversion = 0

        while (len(p) != 0) or (len(q) != 0):
            if len(p) == 0:
                ret.append(q[0])
                q.pop(0)
                continue

            elif len(q) == 0:
                ret.append(p[0])
                p.pop(0)
                continue

            if p[0] > q[0]:
                ret.append(q[0])
                q.pop(0)
                n_inversion += len(p)
            else:
                ret.append(p[0])
                p.pop(0)
            
        return ret, n_inversion

    if l>=r:
        return [seq[l]], 0
    
    m = l + (r-l)//2
    left, n_inversion_left = count_inversion(seq, l, m)
    right, n_inversion_right = count_inversion(seq, m+1, r)
    sorted_arrat, n_inversion = merge(left, right)

    return sorted_arrat, n_inversion_left + n_inversion_right + n_inversion

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split(' ')))
    _, n_inversion = count_inversion(seq = seq, l = 0, r = n-1)
    print(n_inversion)
