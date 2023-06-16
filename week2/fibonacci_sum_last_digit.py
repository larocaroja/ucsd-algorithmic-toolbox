def fibonacci_sum_last_digit(n):
    if n<=1:
        return n
    else:
        one_step_behind = 1
        two_step_behind = 0
        cum_sum = one_step_behind

        for i in range(1, n):
            value = one_step_behind + two_step_behind
            two_step_behind = one_step_behind % 10
            one_step_behind = value % 10
            value = value % 10
            cum_sum += value

    return cum_sum%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_last_digit(n))