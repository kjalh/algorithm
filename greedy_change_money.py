# money = int(input("거스름 돈: "))

# m50000 = money // 50000
# money %= 50000
# print("5만원: ", m50000, "장")

# m10000 = money // 10000
# money %= 10000
# print("1만원: ", m10000, "장")

# m5000 = money // 5000
# money %= 5000
# print("5천원: ", m5000, "장")

# m1000 = money // 1000
# money %= 1000
# print("1천원: ", m1000, "장")

# m500 = money // 500
# money %= 500
# print("5백원: ", m500, "개")

# m100 = money // 100
# money %= 100
# print("1백원: ", m100, "개")

# m50 = money // 50
# money %= 50
# print("5십원: ", m50, "개")

# m10 = money // 10
# money %= 10
# print("1십원: ", m10, "개")


money = int(input("거스름 돈: "))

chg_mon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in chg_mon:
    change = money // i
    money %= i
    
    cnt = "장" if i >= 1000 else "개"
    print(f"{i}원: {change}{cnt}")