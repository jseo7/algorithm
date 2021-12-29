# 3-3 숫자 카드 게임

# 가장 높은 숫자가 쓰인 카드 한장 뽑기
# 1. N x M 형태로 놓임 N : 행의 개수,  M : 열의 개수
# 2. 행 먼저 선택
# 3. 행에 포함된 카드 중 가장 낮은 카드 선택
# 4. 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 가장 높은 숫자 카드를 뽑는 전략 세움

# ex)
# 3  1  2   => 1
# 4  1  4   => 1
# 2  2  2   => 2

# 입력 예시1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력 예시1
# 2

# 입력 예시2
# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 예시2
# 3


##########
# 예시 1
##########
#
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
#
# result = 0
# #한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result) # 최종 답안 출력

##########
# 예시 2
##########

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력