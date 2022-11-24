def solution(genres, plays):
    answer = []
    hash_map = {}
    index = [i for i in range(len(genres))]
    result = []
    for i in zip(genres, plays, index):
        answer.append(i)
    for i in answer:
        if i[0] in hash_map:
            hash_map[i[0]] += i[1]
        else:
            hash_map[i[0]] = i[1]
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    for i in hash_map:
        cnt = 0
        for k in answer:
            if cnt == 2:
                break
            if k[0] == i[0]:
                result.append(k[2])
                cnt += 1

    return result