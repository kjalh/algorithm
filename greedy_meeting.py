for i in range(3):
    print("3번 반복")
    t = input("팀 명: ")
    sm = input("회의 시작 시간: ")
    em = input("회의 종료 시간: ")

    m = []

    if sm > 12:
        sm -= 12
    
    if em > 12:
        em -= 12
    
    m.append((t, sm, em))

result = []

for i in range(3):
    if m[0][2]==m

    