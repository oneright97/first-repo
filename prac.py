# 문자열 메서드 실습 -> print로 출력
# a = ' Practice makes perfect '

# #1. 문자열 a에서 'e'의 개수 세기 ***
# print(a.count('e'))

# #2. 문자열 a에서 i의 위치 찾기(2가지 방법) ***** (im기출)
# print(a.find('i'))
# print(a.index('i'))

# #3. 문자열 a의 문자 사이에 .(점) 삽입 **
# print('.'.join(a))

# #4. 문자열 a를 공백 기준으로 분리하기 ***** (무조건나옴)
# print(a.split())

# #5. 문자열 a에서 'makes'를 'made'로 바꾸기
# print(a.replace('makes', 'made'))

# #6. 문자열 a를 대문자에서 소문자로 바꾸기, 소문자에서 대문자로 바꾸기
# print(a.lower())
# print(a.upper())

# #7. 문자열 a의 양쪽 공백을 없애기 ***
# print(a.strip())

# #8. 입력된 시각(14:43:20)에서 시각 부분만 보여주기 *****
# a = input().split(':')
# print(a[0])

#8-1. 주민등록번호(890927-1212121)에서 생일만 보여주기
# a = '890927-1212121'
# num = a.split('-')
# print(num)
# print(num[0][2:])

# if num[1][0] == '1':
#     print('남성')

# 리스트 메서드 실습
a = ['b', 'a', 'n', 'a', 'n']

# 반환 하지 않는 메서드(void methods)
#1. 리스트 a의 마지막에 'a'추가하기  ***** -> stack(후입선출)
a.append('a')
print(a)

#2-1. 리스트 a를 오름차순으로 정렬 -> 원본을 변경
a.sort()
print(a)

#3. 리스트 a를 내림차순으로 정렬
a.sort(reverse=True)
print(a)

#4. 리스트 a를 역순으로 뒤집기
a.reverse()
print(a)

#5. 리스트 a에서 문자 'a' 삭제하기
a.remove('a')
print(a)

#-------------------------------------------------------------#

# 반환하는 메서드(return methods)
#2-2. 리스트 a를 오름차순으로 정렬 -> 원본을 변경하지 않는다.
print(sorted(a))
print(a)

#6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 반환값 출력 -> 후입선출. 선입선출:popleft
item = a.pop()
print(a)
print(item)

#7. 리스트 a에서 문자 'n'의 개수 출력
count = a.count('n')
print(count)