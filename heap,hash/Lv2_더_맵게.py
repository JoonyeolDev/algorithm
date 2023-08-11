# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 문제 설명
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

scoville, K = [1,2,3,9,10,12], 7 
# return 2


# 2차 수정, heappop+heappush > heappushpop
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return answer
        sum_mins = min_1 + scoville[0] * 2
        heapq.heappushpop(scoville,  sum_mins)
        answer += 1
    return answer if scoville[0] >= K else -1
# 1621.38ms

print(solution(scoville, K))



# 1차 수정, 조건문 정리
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return answer
        min_2 = heapq.heappop(scoville)
        sum_mins = min_1 + min_2 * 2
        heapq.heappush(scoville, sum_mins)
        answer += 1
    return answer if scoville[0] >= K else -1
# 1705.68ms


# 초기 코드, heapq
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        if len(scoville) == 1:
            if scoville[0] >= K: break
            else: return -1
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        if min_1 >= K and min_2 >= K:
            break
        else:
            sum_mins = (min_1 + min_2 * 2)
            heapq.heappush(scoville,sum_mins)
            answer += 1
    return answer
# 1943.20ms




