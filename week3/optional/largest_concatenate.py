def largest_concatenate(seq):
    sorted_seq = sorted(seq, reverse = True)
    
    ret = ''
    for elem in sorted_seq:
        ret = ''.join((ret, str(elem)))

    return int(ret)

if __name__ == '__main__':
    seq = []
    input_ = input()
    for elem in input().split(' '):
        assert len(elem) == 1, f"element of input sequence should be a single-digit number, but got {elem}"
        assert elem.isnumeric(), f"element of input sequence should be a number, but got {elem}"
        seq.append(int(elem))

    largest_combination = largest_concatenate(seq)
    print(largest_combination)