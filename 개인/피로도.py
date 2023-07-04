# 순열 permutations 사용

import itertools

def solution(k, dungeons):
    answer = 0

    for dungeon in itertools.permutations(dungeons, len(dungeons)):
        piro = k
        cnt = 0
        for i in dungeon:
            if piro < i[0]:
                continue
            else:
                piro -= i[1]
                cnt += 1
        if cnt > answer:
            answer = cnt        
    return answer