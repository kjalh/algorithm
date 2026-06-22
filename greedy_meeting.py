print("3번 반복")
m = []

for i in range(3):  
    t = input("팀 명: ")
    sm = int(input("회의 시작 시간: "))
    em = int(input("회의 종료 시간: "))

    
    m.append([t, sm, em])

m.sort(key=lambda x: (x[2], x[1]))


for i in range(2): 
    tmp = m[i+1][2]-m[i+1][1]   # 순수 회의 시간
    m[i+1][1] = m[i][2]         # 앞에 끝난 시간이 다음 시작 시간
    m[i+1][2] = m[i+1][1] + tmp # 시간 배분

for i in range(3):
    print(f"{i+1}번: {m[i][0]}  시간 {m[i][1]} ~ {m[i][2]}")


    