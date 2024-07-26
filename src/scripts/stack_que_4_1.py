"""
https://school.programmers.co.kr/learn/courses/30/lessons/42584

문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.


Parameters 
    prices : List[int]

Constraint 
    prices[i] <= 10,000  as Natural Number 
    2<= len(prices) <= 100,000

Return 
    List[int]


Pseudo Code 

def solution(prices: List[int]) -> List[int]: 
    answer = 0

    1. i 번째 데이터를 i+1 번째부터 빼준다.
    2. if i번째 데이터 뺀값이 >= 0 then 1 else -1
    3. i 번째 데이터 부터 모든 값을 더해준다. 
    4. popleft를 통해 제거해준다. 
    5. 다음번 i+1 번째부터 위 로직을 반복한다. 

    

    return answer 

"""

from math import ceil, floor 
from typing import List, Dict, Tuple
from collections import defaultdict, deque
from operator import itemgetter

prices = [1, 2, 3, 2, 3]
prices = [4, 3, 3, 3, 2, 1]
n = len(prices)
stack = []
answer = [0] * n

def solution(prices: List[int]) -> List[int]: 

    n = len(prices)
    stack = []
    answer = [0] * n

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]: # 전 시점의 가격이 다음 시점보다 클 때 (주가 하락) 
            j = stack.pop()
            answer[j] = i - j
        stack.append(i) # 안떨어진 애들만 확인

    while stack: 
        j = stack.pop()
        answer[j] = n - j - 1 

    return answer

if __name__ == "__main__": 
        
    print(solution(prices))