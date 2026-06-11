import random

def quick(arr):
    # 종료 조건
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    # left 값 > pivot 값 만족 시까지 left 증가(pivot보다 큰 값 찾기) <- pivot보다 작은 것만 왼쪽에 저장
    left = [x for x in arr[1:] if x <= pivot] 

    #  right 값 < pivot 값 만족 시까지 right 감소 <- 마찬기지
    right = [x for x in arr[-1:0:-1] if x > pivot] 
    # right = [x for x in arr[1:] if x > pivot] # 이렇게 해도 결과는 같음
    return quick(left) + [pivot] + quick(right)


def merge(arr):
    # 종료 조건
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 # 반으로 나눔
    left = merge(arr[:mid]) # 인덱스 기준 왼쪽
    right = merge(arr[mid:]) # 인덱스 기준 오른쪽
    
    def merge_div(left, right): # left, right 합치기
        # 종료 조건
        if not left:
            return right
        if not right:
            return left
        
        if left[0] <= right[0]: # 비교해서 더 작은 수 설정
            return [left[0]] + merge_div(left[1:], right)
        else:           
            return [right[0]] + merge_div(left, right[1:])
            
    return merge_div(left, right)


arr = []

for _ in range(7):
    arr.append(random.randint(1,10))


print(f"원본: {arr}")
print("퀵 정렬: ", quick(arr.copy()))
print("병합정렬: ", merge(arr.copy()))