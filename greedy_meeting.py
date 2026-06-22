for i in range(3):
    print("3번 반복")
    t = input("팀 명: ")
    sm = int(input("회의 시작 시간: "))
    em = int(input("회의 종료 시간: "))

    m = []

    if sm > 12:
        sm -= 12
    
    if em > 12:
        em -= 12
    
    m.append(t, sm, em)


m.sort(x= lambda x: x[2])
    


for i in range(3):
    print(f"{i+1}번: {m[i][0]}")


    