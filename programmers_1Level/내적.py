def solution(a, b):
    # return sum([a[i]*b[i]for i in range(len(a))])
    return sum([a * b for a, b in zip(a, b)])