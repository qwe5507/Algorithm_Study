# 프로그래머스 코딩테스트 연습
# 스택/큐
# 기능개발


def solution(progresses, speeds):
    answer = []
    count = 1

    result = 0
    for i in range(len(progresses)):

        temp = progresses[i] + speeds[i] * count
        while temp < 100:
            temp = progresses[i] + speeds[i] * count
            count += 1

    return answer