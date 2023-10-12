import random

correct = random.randrange(100)

ans = -1  # 아직 정답을 맞추지 못함
num = 0

while ans != correct and num < 11:
    ans = int(input("숫자를 입력하세요 (범위:0~99) : "))
    num += 1
    if ans < correct:
        print("아닙니다. 더 큰 숫자입니다!")
    elif ans > correct:
        print("아닙니다. 더 작은 숫자입니다!")
    else:
        print("정답입니다. %d번만에 맞추셨습니다." %num)
        print("게임이 끝났습니다.")
        