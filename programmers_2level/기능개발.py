# 프로그래머스 코딩테스트 연습
# 스택/큐
# 기능개발

# 너무 비효율적인 코드인것 같다 ..
def solution(progresses, speeds):
    answer = []
    count = 1

    result = 0
    flag = True
    for i in range(len(progresses)):

        temp = progresses[i] + speeds[i] * count

        while temp < 100:
            flag = False
            temp = progresses[i] + speeds[i] * count
            count += 1

        if flag:
            answer.append(result)
            result = 0
        result += 1

        flag = True

    return answer