def binary_search(K, q, l, r):
    if r - l <= 1:
        if K[l] == q:
            return l
        else:
            return -1

    mid = l + (r - l)//2
    # print(l,r,mid)
    elem_mid = K[mid]

    if elem_mid == q:
        return mid
    
    elif elem_mid > q: # q may be located between [l, mid)
        l  = l
        r = mid-1
        return binary_search(K, q, l, r)
    
    else: # q may be located between (mid, r]
        l = mid + 1
        r = r
        return binary_search(K, q, l, r)

if  __name__ == "__main__":
    n = int(input())
    K = list(map(int, input().split(' ')))
    m = int(input())
    Q = list(map(int, input().split(' ')))

    for i, q in enumerate(Q):
        if i != m-1:
            print(binary_search(K, q, 0, n-1), end = ' ')
        else:
            print(binary_search(K, q, 0, n-1))