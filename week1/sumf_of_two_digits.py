def sum_of_two_digits(a, b):
    return a + b


if __name__ == '__main__':
    input_string = input()
    a, b = map(int, input_string.split(' '))
    print(sum_of_two_digits(a,b))