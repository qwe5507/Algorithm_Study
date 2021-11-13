# 프로그래머스 level 1문제 부족한 금액 계산하기.

def solution(price, money, count):
    # total = 0
    # for i in range(1,count+1):
    #     total += price*i
    total = sum([ price * i for i in range(1,count+1)])
    if total > money:
        return total-money
    else :
        return 0


# 다른사람 풀이

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
# total에서 money를빼는게 아니라, money에서 total을뺀후 total이큰경우 는 - 값이나오게해 최소값으로 출력되고
# money가더 큰경우는 정수가 나오게해 0이 출력되게해서 절대값을 구한다
