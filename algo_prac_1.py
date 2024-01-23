# def sum_odd(numbers):
#     odd_num = 0
#     for num in numbers:
#         if num % 2 != 0:
#             odd_num += num
#     return odd_num


# T = int(input())
# for tc in range(1, T + 1):
#     numbers = list(map(int, input().split()))
#     result = sum_odd(numbers)

#     print(f'#{tc} {result}')

def find_max_num(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
