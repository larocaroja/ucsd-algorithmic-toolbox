def binary_search_with_duplicates(K, q, l, r, last_result = (-1, -1)):
    if r - l < 1:
        if K[l] == q:
            return l
        elif last_result[0] == q:
            return last_result[1]
        else:
            return -1

    mid = l + (r - l)//2
    elem_mid = K[mid]
    
    if elem_mid >= q: # q may be located between [l, mid)
        if elem_mid == q:
            last_result = (elem_mid, mid)
        l  = l
        r = mid-1
        return binary_search_with_duplicates(K, q, l, r, last_result = last_result)
    
    else: # q may be located between (mid, r]
        l = mid + 1
        r = r
        return binary_search_with_duplicates(K, q, l, r, last_result = last_result)

if  __name__ == "__main__":
    n = int(input())
    K = list(map(int, input().split(' ')))
    m = int(input())
    Q = list(map(int, input().split(' ')))

    print(' '.join([str(binary_search_with_duplicates(K, q, 0, n-1)) for q in Q]))