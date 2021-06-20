import random

print("'우스꽝스러운 이름 만들기 프로젝트'에 오신것을 환영합니다!")
print("아래에 선정된 별명이 마음에 들면 'N'을 눌러주세요. 3번째 수정본")

First = ('꿀꿀이', '음메', '바보', '똥멍청이', '비브라늄', '가디언', '엔젤', '다크나이트', '호구', '하하하')
Last = ('김', '이', '박', '최', '송', '백', '피', '파', '차', '병', '가', '나', '다')

while True:
    First_Name = random.choice(First)
    Last_Name = random.choice(Last)
    print("{0},{1}".format(First_Name, Last_Name))
    Test = input("별명을 다시 지어드릴까요? 'Y or N'을 눌러주세요.")
    
    if Test.lower() == "n":
        break
    print()

input("그러면 이만~")