"""

문제 설명
배열에서 각 요소에 대해 오른쪽에 있는 첫 번째 큰 숫자를 찾는 문제입니다. 주어진 배열 nums에서 각 요소 nums[i]의 "오큰수"는 
그 요소보다 오른쪽에 있는 첫 번째 더 큰 요소입니다. 
만약 그러한 요소가 없다면, -1을 반환합니다.

조건
배열의 각 요소에 대해 오른쪽에 있는 첫 번째 큰 숫자를 찾습니다.
현재 숫자가 스택에 저장된 숫자보다 크면, 스택에서 요소를 제거하고 해당 인덱스의 오큰수를 현재 숫자로 설정합니다.
각 요소를 스택에 저장하면서 오른쪽에 있는 첫 번째 큰 숫자를 찾기 위해 비교합니다.
입력
배열 nums가 주어집니다. 배열의 크기는 1 이상 10,000 이하입니다.
배열의 각 요소는 1 이상 1,000,000 이하의 정수입니다.
출력
각 요소의 오큰수를 담은 배열을 반환합니다.
예제
입력: [2, 1, 2, 4, 3]
출력: [4, 2, 4, -1, -1]

설명
nums[0] = 2의 오큰수는 4 (2의 오른쪽에서 첫 번째로 큰 숫자).
nums[1] = 1의 오큰수는 2 (1의 오른쪽에서 첫 번째로 큰 숫자).
nums[2] = 2의 오큰수는 4 (2의 오른쪽에서 첫 번째로 큰 숫자).
nums[3] = 4의 오큰수는 없음 (-1).
nums[4] = 3의 오큰수는 없음 (-1).

"""

# 첫번쨰로 큰수가 나오면 조건을 만족하고 pop 
# 해당 인덱스 조건을 만족하면 계속해서 제거 while
# 다음 인덱스를 다시 stack 에 저장 
# 해당 인덱스 조건에 맞는 answer에 값을 append
# 조건에 맞지 않은 애들의 인덱스는 -1 로 반환 

from typing import List, Dict, Tuple 
from collections import defaultdict, deque

nums = [2, 1, 2, 4, 3]

def solution(nums: List[int]) -> List[int]: 
    stack = []
    n = len(nums)
    answer = [-1] * n 

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]: # i가 stack의 최신값보다 클 떄 
            j = stack.pop()
            answer[j] = nums[i]
        stack.append(i)

    return answer 

solution(nums)