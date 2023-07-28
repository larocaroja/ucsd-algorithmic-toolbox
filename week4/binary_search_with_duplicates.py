def binary_search_with_duplicates(K, q, l, r, prev = (-1, -1)):
    if r - l <= 1:
        if K[l] == q:
            return l
        elif prev[0] == q:
            return prev[1]
        else:
            return -1

    mid = l + (r - l)//2
    elem_mid = K[mid]
    
    if (prev[0] == q) and (elem_mid != q):
        return prev[1]
    
    if elem_mid >= q: # q may be located between [l, mid)
        l  = l
        r = mid-1
        return binary_search_with_duplicates(K, q, l, r, prev = (elem_mid, mid))
    
    else: # q may be located between (mid, r]
        l = mid + 1
        r = r
        return binary_search_with_duplicates(K, q, l, r, prev = (elem_mid, mid))

if  __name__ == "__main__":
    n = int(input())
    K = list(map(int, input().split(' ')))
    m = int(input())
    Q = list(map(int, input().split(' ')))

    for i, q in enumerate(Q):
        if i != m-1:
            print(binary_search_with_duplicates(K, q, 0, n-1), end = ' ')
        else:
            print(binary_search_with_duplicates(K, q, 0, n-1))