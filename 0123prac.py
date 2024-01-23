# a = [1, 2, 3]
# b = [4, 5, 6]

# a.append(b)
# print(a)

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())

#     # arr = []
#     # for i in range(N):
#     #     row = list(map(int, input().split()))
#     #     arr.append(row)
    
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     code ~~~~~

#     print(f'{tc} {result}')

my_dict = {
    'plus' : ['더하기', '장점'],
    'minus' : ['빼기', '적자'],
    'multiply' : ['곱하기', '다양하게'],
    'division' : ['나누기', '분열']
}

#실습 1. '빼기' 반환 (4가지 방법)
# print(my_dict.get('minus')[0])
# print(list(my_dict.values())[1][0])
# print(my_dict.pop('minus')[0])
# # print(my_dict.setdefault('minus')[0])

#실습 2. key값 순차적으로 출력 (for문 사용)
# my_keys = list(my_dict.keys())
# for key in my_keys:
#     print(key)

#실습 3. 'square' : ['제곱', '사각형'] 추가 (4가지 방법)
# my_dict.setdefault('square', ['제곱', '사각형'])
# my_dict.update({'square': ['제곱', '사각형']})
# print(my_dict)

#실습 4. 'division' 제거 (2가지 방법)
# my_dict.pop('division')
# del my_dict['division']
# print(my_dict)