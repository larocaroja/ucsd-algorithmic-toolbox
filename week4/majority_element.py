def majority_element(seq, l, r):
    if l>=r:
        return seq[l]
    
    mid = l + (r-l)//2
    left = majority_element(seq, l, mid)
    right = majority_element(seq, mid+1, r)

    if left == right:
        return left

    else:
        left_count = sum([1 for v in seq[l:r+1] if v == left])
        right_count = sum([1 for v in seq[l:r+1] if v == right])

        if left_count > (r-l+1)//2:
            return left
        elif right_count > (r-l+1)//2:
            return right
        else:
            return -1
        
def majority_element_iterative(seq):
    count = dict()

    for v in seq:
        if v not in count.keys():
            count[v] = 1
        else:
            count[v] += 1

    max_freq = -1
    max_value = -1

    for element, occurence in count.items():
        if occurence > max_freq:
            max_freq = occurence
            max_value = element
    
    if max_freq > len(seq)//2:
        return max_value
    else:
        return -1
    

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split(' ')))

    major_elem = majority_element(seq, l = 0, r = n-1)
    
    if major_elem != -1:
        print(1)
    else:
        print(0)