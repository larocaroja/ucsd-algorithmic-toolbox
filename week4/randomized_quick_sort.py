import random

def randomized_quick_sort(seq, l, r):
    def partition3(seq, l, r):
        pivot = random.choice(range(l, r+1))
        seq[l], seq[pivot] = seq[pivot], seq[l]
        
        elem_pivot = seq[l]
        n_duplicates = 0
        j = l

        for i in range(l+1, r+1):
            if seq[i] < elem_pivot:
                j += 1
                seq[j], seq[i] = seq[i], seq[j]
            elif seq[i] == elem_pivot:
                n_duplicates += 1
                j += 1
                seq[l+n_duplicates], seq[l+n_duplicates+1:i+1] = seq[i], seq[l+n_duplicates:i]

        for k in range(n_duplicates+1):

            seq[l+k], seq[j-k] = seq[j-k], seq[l+k]

        return seq, j-n_duplicates, j
    
    if l>r:
        return []
    elif l == r:
        return [seq[l]]

    seq, m1, m2 = partition3(seq, l, r)

    left = randomized_quick_sort(seq, l, m1-1)
    right = randomized_quick_sort(seq, m2+1, r)
    mid = seq[m1:m2+1]

    return left + mid + right

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split(' ')))
    print(' '.join(randomized_quick_sort(seq = seq, l = 0, r = n-1)))
    