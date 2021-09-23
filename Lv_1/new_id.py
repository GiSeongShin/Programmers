# my solution
import re


def remove_first_last_dot(plain_text):
    while plain_text[0] == "." or plain_text[-1] == ".":
        if plain_text == ".":
            plain_text = ""
            return plain_text
        elif plain_text[0] == ".":
            plain_text = plain_text[1:]
        elif plain_text[-1] == ".":
            plain_text = plain_text[:-1]

    return plain_text


def solution(new_id):
    if len(new_id) != 0:
        # 1단계 new_id 의 모든 대문자를 대응되는 소문자로 치환합니다.
        new_id = new_id.lower()
        # 2단계 new_id 에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        p = re.compile('[^0-9a-z-_.]')
        new_id = re.sub(p, "", new_id)
        # 3단계 new_id 에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
        while ".." in new_id:
            new_id = new_id.replace("..", ".")
    else:
        new_id = "a"

    # 4단계 new_id 에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    # print(new_id)
    new_id = remove_first_last_dot(new_id)

    # 5단계 new_id 가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = "a"

    # 6단계 new_id 의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    # 7단계 new_id 의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    elif len(new_id) >= 16:
        new_id = remove_first_last_dot(new_id[:15])

    return new_id


# best solution
def solution(new_id):
    st = new_id
    st = st.lower()
    # a-z 알파벳 & 0-9 숫자 & -_. 을 제외한 문자를 '' 으로 변환
    st = re.sub('[^a-z0-9\-_.]', '', st)
    # .+ 를 사용하면 . 뒤에 .이 나오는지 체크한다.
    # . 뒤에 . 이 나오면 '.' 으로 변환
    st = re.sub('\.+', '.', st)
    # ^ 는 문자의 시작 / $ 는 문자의 마지막을 의미한다.
    # ^[.] --> 시작이 . 인 것 / [.]$ --> 마지막이 . 인 것
    # 처음과 마지막이 . 이면 '' 으로 변환
    st = re.sub('^[.]|[.]$', '', st)
    # 5, 6단계
    # list slicing 에서 끝 인덱스는 범위를 벗어난 인덱스를 지정할 수 있음
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    # 7단계
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st