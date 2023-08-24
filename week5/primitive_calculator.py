N_OPERATIONS = dict()
N_OPERATIONS[1] = 0

def step(i):
    is_multiple_2 = (i/2).is_integer()
    is_multiple_3 = (i/3).is_integer()

    operations = [i-1]
    if is_multiple_2:
        operations.append(int(i/2))
    if is_multiple_3:
        operations.append(int(i/3))

    n_operation_prev = []
    for operation in operations:
        n_operation_prev.append(N_OPERATIONS[operation] + 1)

    return min(n_operation_prev)

def primitive_calculator(n):
    if n <= 0:
        return -1
    
    for i in range(2, n+1):
        N_OPERATIONS[i] = step(i)

    return N_OPERATIONS[n]

def reconstruct_sequence(n):
    sequence = []

    current = n
    sequence.append(current)

    while current != 1:
        current_n_operation = N_OPERATIONS[current]
        is_multiple_2 = (current/2).is_integer()
        is_multiple_3 = (current/3).is_integer()
        
        operations = [current-1]
        if is_multiple_2:
            operations.append(int(current/2))
        if is_multiple_3:
            operations.append(int(current/3))

        for operation in operations:
            if N_OPERATIONS[operation] + 1 == current_n_operation:
                current = operation
        
        sequence.append(current)
        
    return sequence[::-1]



if __name__ == '__main__':
    n = int(input())

    n_operation = primitive_calculator(n)
    print(n_operation)
    if n_operation != -1:
        print(' '.join(map(str, reconstruct_sequence(n))))