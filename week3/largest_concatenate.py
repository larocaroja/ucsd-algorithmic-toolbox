def largest_concatenate_single_digit(seq):
    sorted_seq = sorted(seq, reverse = True)
    
    ret = ''
    for elem in sorted_seq:
        ret = ''.join((ret, str(elem)))

    return int(ret)

def largest_concatenate(seq):
    def _is_better(n, m):
        n, m = str(n), str(m)
        if int(''.join([n, m])) >= int(''.join([m, n])):
            return True
        else:
            return False
    
    ret_seq = []
    while len(seq) != 0:
        max_number = 0
        for element in seq:
            if _is_better(element, max_number):
                max_number = element

        ret_seq.append(max_number)
        seq.remove(max_number)
        
    return ''.join(map(str, ret_seq))

if __name__ == '__main__':
    seq = []
    input_ = input()
    seq = list(map(int, input().split(' ')))
    # for elem in input().split(' '):
    #     assert len(elem) == 1, f"element of input sequence should be a single-digit number, but got {elem}"
    #     assert elem.isnumeric(), f"element of input sequence should be a number, but got {elem}"
    #     seq.append(int(elem))

    largest_combination = largest_concatenate(seq)
    print(largest_combination)