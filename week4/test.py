def find_majority_element(nums):
    def majority_element_rec(lo, hi):
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]

        # recurse on left and right halves of this slice.
        mid = (hi-lo)//2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid+1, hi)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

        if left_count > (hi-lo+1) // 2:
            return left
        elif right_count > (hi-lo+1) // 2:
            return right
        else:
            return 0

    return majority_element_rec(0, len(nums)-1)

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split(' ')))

    print(find_majority_element(seq))