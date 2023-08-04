# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
# result = 8

answer=0
bridge = [0]*bridge_length
idx = 0
count=0
sum_weight = 0
while len(truck_weights)>count:
    answer+=1
    try:
        if weight >= (sum_weight+truck_weights[idx]-bridge[-1]):
            bridge.insert(0,truck_weights[idx])
            sum_weight+=truck_weights[idx]
            idx+=1
        else:
            bridge.insert(0,0)
    except:
        bridge.insert(0,0)
    if len(bridge)>=bridge_length:
        a = bridge.pop()
        if a in truck_weights:
            count+=1
            sum_weight-=a
    
    print(bridge,idx,sum_weight)


# deque, appendleft, pop 쓰는게 시간상 더 이득
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge = deque([0]*bridge_length)
    idx = 0
    count=0
    sum_weight = 0
    while len(truck_weights)>count:
        answer+=1
        try:
            if weight >= (sum_weight+truck_weights[idx]-bridge[-1]):
                bridge.appendleft(truck_weights[idx])
                sum_weight+=truck_weights[idx]
                idx+=1
            else:
                bridge.appendleft(0)
        except:
            bridge.appendleft(0)
        if len(bridge)>=bridge_length:
            a = bridge.pop()
            if a in truck_weights:
                count+=1
                sum_weight-=a
    return answer

# list, insert, pop
# def solution(bridge_length, weight, truck_weights):
#     answer=0
#     bridge = [0]*bridge_length
#     idx = 0
#     count=0
#     sum_weight = 0
#     while len(truck_weights)>count:
#         answer+=1
#         try:
#             if weight >= (sum_weight+truck_weights[idx]-bridge[-1]):
#                 bridge.insert(0,truck_weights[idx])
#                 sum_weight+=truck_weights[idx]
#                 idx+=1
#             else:
#                 bridge.insert(0,0)
#         except:
#             bridge.insert(0,0)
#         if len(bridge)>=bridge_length:
#             a = bridge.pop()
#             if a in truck_weights:
#                 count+=1
#                 sum_weight-=a
#     return answer