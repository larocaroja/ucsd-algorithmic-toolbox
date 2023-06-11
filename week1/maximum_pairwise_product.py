def maximum_pairwise_product(seq):
    greatest_1 = 0
    greatest_2 = 0

    for v in seq:
        if v >= greatest_1:
            greatest_2 = greatest_1
            greatest_1 = v

        elif v >= greatest_2:
            greatest_2 = v

    return greatest_1*greatest_2

if __name__ == '__main__':
    _ = int(input())
    seq = list(map(int, input().split()))

    print(maximum_pairwise_product(seq))