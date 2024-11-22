# 코딩톡

def find_non_readers(n, m, p, messages):
    # p번째 메시지의 읽지 않은 사람 수
    unread_count_p = messages[p - 1][1]

    # 읽지 않은 사람이 없으면 바로 종료
    if unread_count_p == 0:
        return ""

    # 읽지 않은 사람을 저장할 리스트
    non_readers = []

    # 각 사람에 대해 확인 ('A'부터 'A+n-1')
    for i in range(n):
        person = chr(65 + i)  # 사람 이름
        read = False

        # 메시지 확인
        for j in range(m):
            sender, unread_count = messages[j]
            if unread_count >= unread_count_p and sender == person:
                read = True
                break

        # 읽지 않은 사람으로 간주
        if not read:
            non_readers.append(person)

    # 사전순 정렬 후 반환
    return " ".join(non_readers)


# 입력 처리
n, m, p = map(int, input().split())
messages = [input().split() for _ in range(m)]
messages = [(msg[0], int(msg[1])) for msg in messages]

# 결과 출력
print(find_non_readers(n, m, p, messages))
