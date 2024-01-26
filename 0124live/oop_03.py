# 실습 1

# class Singer:
#     # job = 'singer' # 클래스 변수

#     def __init__(self):
#         self.occ = '가수' # 멤버 변수
#         self.country = '대한민국' # 멤버 변수
#         self.bday = '1993년 5월 16일' # 멤버 변수

#     def rapping(self):
#         # return f'{self.name}가 랩을 합니다.'
#         print('랩 하기')
    
#     def dancing(self):
#         # return f'{self.name}가 춤을 춥니다.'
#         print('춤 추기')
    
#     def singing(self):
#         # return f'{self.name}가 노래를 부릅니다.'
#         print('노래 하기')
    
# singer = Singer()

# print('직업: ', singer.occ)
# print('생년월일: ', singer.bday)
# print('국적: ', singer.country)

# singer.rapping()
# singer.singing()
# singer.dancing()

# # singer1 = Singer('iu', 'Korea', '1993년 5월 16일')
# # singer2 = Singer('bts', 'Korea', '1997년 1월 21일')
# # singer3 = Singer('zico', 'Korea', '1995년 6월 6일')

# # print(singer1.singing())
# # print(singer2.dancing())
# # print(singer3.rapping())

# # print(singer1.country)



# 실습2. 
# my_count라는 메서드 직접 만들기
# 클래스 명은 my_str

# 조건 1. 생성자 메서드 구조
# 조건 2. 클래스 변수와 멤버 구조

# class MyStr:

#     count = 0
#     def __init__(self, string) -> None:
#         # 멤버 변수 string를 생성자에서 초기화
#         self.string = string

#     def my_count(self, char):
#         self.count = self.string.count(char)
#         return self.count
#     # self.count와 self.string.count의 차이? 멤버변수 self.string 초기화 이유는?
#     # 클래스 변수 count는 반드시 있어야 하나? 없어도 됨.
#     # 클래스 변수의 역할 : 클래스 변수로 데이터를 추적하거나 데이터를 공유
#     # 멤버 변수의 역할 : 멤버 변수로 데이터를 추적하거나 데이터의 개별화
# my_str = input()
# my_instance = MyStr(my_str)
# result = my_instance.my_count('i')
# print(result)



# 실습3. 클래스 메서드
# class Singer:
#     occ = '가수'
#     country = '대한민국'
#     bday = "1993년 5월 16일"

#     @classmethod
#     def rapping(cls):
#         # return f'{self.name}가 랩을 합니다.'
#         print('랩 하기')
    
#     @classmethod
#     def dancing(cls):
#         # return f'{self.name}가 춤을 춥니다.'
#         print('춤 추기')
    
#     @classmethod
#     def singing(cls):
#         # return f'{self.name}가 노래를 부릅니다.'
#         print('노래 하기')

# singer = Singer()

# print('직업: ', singer.occ)
# print('생년월일: ', singer.bday)
# print('국적: ', singer.country)

#실습4. 스태틱메서드 : 클래스나 인스턴스와는 무관하게 독립적으로 동작
#클래스 내부에서 선언되지만 클래스 변수에 접근하지 않는다

class Singer:
    occ = '가수'
    country = '대한민국'
    bday = "1993년 5월 16일"

    @staticmethod
    def rapping():
        # return f'{self.name}가 랩을 합니다.'
        print('랩 하기')
    
    @staticmethod
    def dancing():
        # return f'{self.name}가 춤을 춥니다.'
        print('춤 추기')
    
    @staticmethod
    def singing():
        # return f'{self.name}가 노래를 부릅니다.'
        print('노래 하기')

singer = Singer()

print('직업: ', singer.occ)
print('생년월일: ', singer.bday)
print('국적: ', singer.country)