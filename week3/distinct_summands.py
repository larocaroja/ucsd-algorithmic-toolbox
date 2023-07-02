def distinct_summands(n):
    sequence_sum = 0
    last_summand = 0
    sequence_length = 0
    sequence = []

    while sequence_sum < n:
        if n - sequence_sum < last_summand + 1:
            left = n - sequence_sum
            sequence[-1] += left

            break
        
        else:
            last_summand += 1
            sequence.append(last_summand)
            sequence_sum += last_summand
            sequence_length += 1

    return sequence_length, sequence

if __name__ == "__main__":
    n = int(input())
    sequence_length, sequence = distinct_summands(n)
    print(sequence_length)
    print(' '.join(map(str, sequence)))