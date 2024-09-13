def sum_a_b(a, b):
    sum = a + b
    return sum

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_a_b(a,b))