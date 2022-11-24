#런타임 에러남
def solution(genres, plays):
    answer = []
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i])#실행횟수, 고유번호
        else : #초기화를 위해서 첫번째 애들은 넣고 시작
            dic[genres[i]] = [[plays[i],i]] #실행횟수, 고유번호
    # print(dic)

    genre_rank ={}
    for genre in dic:
        songs=dic[genre]
        play_sum=0
        for song in songs:
            play_sum+=song[0]
        genre_rank[genre]=play_sum
    #genre_rank를 재생 횟수가 큰 순으로 정렬 
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    # print(genre_rank)
    for genre in genre_rank:
        song_rank=sorted(dic[genre[0]], key=lambda x:(-x[0],x[1]))
        print(song_rank)
        for i in range(2):
            answer.append(song_rank[i][1])
    return answer