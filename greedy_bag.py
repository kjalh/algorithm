max_weight = 16

mul = []

print("3번 반복")
for i in range(3):
    n = input("물건 입력: ")
    w = int(input("물건 무게(kg): "))
    m = int(input("총 가격: "))

    mul.append([n, w, m])


mul.sort(key=lambda x: x[2] / x[1], reverse=True)

total = 0 

for i in mul:
    name, weight, price = i
    
    if max_weight >= weight:
        max_weight -= weight
        total += price
        print(f"-> {name} {weight}kg 전부 담음 (남은 배낭: {max_weight}kg)")
    else:
        div = max_weight / weight 
        total += price * div
        print(f"-> {name} {max_weight}kg 만큼만 잘라서 담음 (배낭 꽉 참)")
        break 

print(f"최종 가방의 가치: {total}원")
