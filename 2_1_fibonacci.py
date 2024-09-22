def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        fib_list = [0,1]
        for i in range(2,n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
