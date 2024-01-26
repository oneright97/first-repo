# 45분 알람 일찍 설정하기

my_list = input().split()

H = int(my_list[0])
M = int(my_list[1])

0 <= H <= 23
0 <= M <= 59

if M >= 45:
    alarm_M = M - 45
    print(H, alarm_M)
else:
    remain = 45 - M
    alarm_M = 60 - remain
    H -= 1
    if H < 0:
        H = 23
    print(H, alarm_M)
