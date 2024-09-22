def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_number_index = 0
    max_number_first = 0
    max_number_second = 0
    for i in range(n):
        if numbers[i] > max_number_first:
            max_number_first = numbers[i]
            max_number_index = i
    
    for a in range(n):
        if numbers[a] > max_number_second and a != max_number_index:
            max_number_second = numbers[a]

    return max_number_first*max_number_second

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast(input_numbers))

