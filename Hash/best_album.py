from operator import itemgetter


def solution(genres, plays):
    genres_dict = {}
    for idx, genre in enumerate(genres):
        if genre in genres_dict.keys():
            genres_dict[genre].append({"idx": idx, "count": plays[idx]})
        else:
            genres_dict[genre] = [{"idx": idx, "count": plays[idx]}]

    # 장르별 재생횟수의 합 구하기
    count_of_genres = []
    for genre in genres_dict.keys():
        # 재생횟수의 합을 구할 때 루프가 돌기 때문에
        # 장르별 노래들의 count 를 이용해 정렬해준다
        # count 가 같으면 idx 순으로 정렬한다고 했기 때문에 sort 조건은 count, idx 이다.
        genres_dict[genre].sort(key=itemgetter('count', 'idx'), reverse=True)
        count_of_play = 0
        for song in genres_dict[genre]:
            count_of_play += song['count']

        count_of_genres.append({'genre': genre, 'count': count_of_play})

    # 장르별 재생횟수의 합을 순서대로 정렬하면 베스트 장르순으로 정렬된다.
    sorted_genres = sorted(count_of_genres, key=itemgetter('count'), reverse=True)

    best_genres = []
    for genre in sorted_genres:
        best_genres.append(genre['genre'])

    # 장르 별 베스트 2개씩 베스트앨범에 추가
    answer = []
    for genre in best_genres:
        song_count = 0
        for song in genres_dict[genre]:
            if song_count == 2:
                break

            answer.append(song['idx'])
            song_count += 1

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)
