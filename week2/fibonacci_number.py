def fibonacci_number_recursion_with_memoriazation(n, lookup = dict()):
    print(n, lookup)
    if n <= 1:
        return n
    
    if n in lookup.keys():
        return lookup[n]

    else:
        lookup[n] = fibonacci_number_recursion_with_memoriazation(n-1, lookup) + fibonacci_number_recursion_with_memoriazation(n-2, lookup)
        return lookup[n]
    
def fibonacci_number_iternative(n):
    if n<=1:
        return n
    else:
        one_step_behind = 1
        two_step_behind = 0

        for _ in range(1, n):
            value = one_step_behind + two_step_behind
            two_step_behind = one_step_behind
            one_step_behind = value

    return value

if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_number_recursion_with_memoriazation(n))
    print(fibonacci_number_iternative(n))