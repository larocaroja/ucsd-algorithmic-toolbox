# key lemma
# a = a' + bq for some q
# d divides a and b if and only if it divides a' and b

def gcd(a, b):
    if b == 0:
        return a
    
    a_prime = a%b
    return gcd(b, a_prime)

if __name__ == '__main__':
    a, b = map(int, input().split(' '))

    if a>b:
        big = a
        small = b
    else:
        big = b
        small = a

    print(gcd(big, small))