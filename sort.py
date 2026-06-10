import random

def BUBBLE_ASC(arr):
    a = 0
    while True:
        swp = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swp = True
                a+=1
        if not swp:
            break

    return f"버블 오름차순: {arr}, 정렬 횟수: {a}"

def BUBBLE_DESC(arr):
    a = 0
    while True:
        swp = False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swp = True
                a+=1
        if not swp:
            break

    return f"버블 내림차순: {arr}, 정렬 횟수: {a}"

def SELECT_ASC(arr):
    a = 0
    for i in range(len(arr)-1):
        min_idx = i 

        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j  
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            a += 1 
            
    return f"선택 오름차순: {arr}, 정렬 횟수: {a}"

def SELECT_DESC(arr):
    a=0
    for i in range(len(arr)-1):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[max_idx] < arr[j]:
                max_idx = j
        
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            a+=1
            
    return f"선택 내림차순: {arr}, 정렬 횟수: {a}"

def INSERT_ASC(arr):
    a=0
    for i in range(1, len(arr)):
        j = i-1
        tmp = arr[i]
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j-=1
            a+=1
        arr[j+1] = tmp
    return f"삽입 오름차순: {arr}, 정렬 횟수: {a}"


def INSERT_DESC(arr):
    a=0
    for i in range(1, len(arr)):
        j = i-1
        tmp = arr[i]
        while j >= 0 and arr[j] <tmp:
            arr[j+1] = arr[j]
            j-=1
            a+=1
        arr[j+1] = tmp
        
    return f"삽입 내림차순: {arr}, 정렬 횟수: {a}"

arr = []

for _ in range(5):
    arr.append(random.randint(1,10))


print(f"원본: {arr}")
print(BUBBLE_ASC(arr.copy()))
print(BUBBLE_DESC(arr.copy()))
print()
print(SELECT_ASC(arr.copy()))
print(SELECT_DESC(arr.copy()))
print()
print(INSERT_ASC(arr.copy()))
print(INSERT_DESC(arr.copy()))

