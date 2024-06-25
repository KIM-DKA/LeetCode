"""

https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다. (장르의 플레이 횟수인건지..각 플레이 숫자가 unique )
입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
입출력 예 설명

classic 장르는 1,450회 재생되었으며
고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생

pop 장르는 3,100회 재생되었으며, 
고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생

pop 장르의 [4, 1]번 노래를 먼저, 
classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.

Parameter  
    genres: List[str] - 노래 장르 리스트 
    plays: List[int] - 노래 플레이 리스트 

Algorithm 

    Init genre_play_count : defaultdict(int) - 각 장르 총 재생수 
    Init genre_song_list : defaultdict(int) - 각 장르별로 (노래 고유번호, play수)

    1. 가장 많이 재생된 장르를 내림 차순으로 정리

    for 장르 in genres: 
        genre_play_count[장르] = sum(play 수)
        genre_song_list[장르].append((고유번호,플레이수)) 
    
    2. 가장 많이 재생된 장르 정렬 
        genre_play_count.sort(by)

    3. 각 장르별 (노래 고유번호, play수) 를 정렬하되 play 수가 같으면 낮은 고유번호 

    4. 베스트 앨범 추출 장르 내에 노래가 1개면 1개만 수록

Return 
    best_album: List[int] 

이 문제에서 배울 것 

1. from typing import List, Dict, Tuple 과 같은 여러가지 타입 힌트 
2. operator 에서 itemgetter를 key 로 둬서 sort하기 
3. 딕셔너리 안에 데이터 타입을 좀더 유도리 있게 가져 갈 것 genre_song_list: Dict[str, List[Tuple(int, int)]]
4. list 에 append 대신 extend 를 쓴다면 요소를 전부 더해주기 편함
5. 만약 정렬해야 되는 조건이 2개인 경우에는 lambda x: (-x[1],x[0])를 기억은 해주면 좋을지도.. 앞에 플레이 카운트는 내림차순, 뒤에 고유 번호는 오름 차순

"""



from typing import List, Dict, Tuple
from collections import defaultdict 
from operator import itemgetter

def solution(genres: List[str], plays: List[int]) -> List[int]: 

    genre_play_count = defaultdict(int)
    genre_song_list = defaultdict(list)

    # 장르별 합계, 장르별 (고유번호, 플레이 수)
    for i, (genre, play_count) in enumerate(zip(genres,plays)): 
        genre_play_count[genre] += play_count
        genre_song_list[genre].append((i,play_count))

    # 장르별 합계순으로 정렬 
    genre_sorted = [genre for genre, play_count in sorted(genre_play_count.items(), key=itemgetter(1), reverse=True)]

    # 장르 내에서 고유번호와 플레이 카운트도 정렬 

    for genre in genre_song_list: 
        genre_song_list[genre].sort(key=itemgetter(0), reverse=False) # 플레이 숫자가 큰 숫자부터 (오름차순)
        genre_song_list[genre].sort(key=itemgetter(1), reverse=True) # 플레이 숫자가 큰 숫자부터 (내림차순)

    
    # 장르 플레이 된 순에서 Top2 까지 추출 

    best_album = []

    for genre in genre_sorted: 
        best_album.extend([x[0] for x in genre_song_list[genre][:2]])

    return best_album



if __name__ == '__main__':

    genres = ["classic", "pop", "classic", "classic", "pop", "kpop"]
    plays = [150, 600, 150, 800, 2500, 10000]

    print(solution(genres, plays))
