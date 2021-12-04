# 프로그래머스 Level 2 , 가장 큰 수
#

def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer


if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))

    # print('2022' < '2202')
    print('222' > '2222')