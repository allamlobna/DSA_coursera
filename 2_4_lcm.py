def lcm(a, b):
    c = a*b
    while a%b != 0:
        a, b = b, a%b
    return int(c/b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

