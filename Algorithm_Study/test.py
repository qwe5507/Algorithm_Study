import re


def solution(time, plans):
    answer = ''

    for name, start, end in plans:
        total = 0
        startNum = int(re.sub(r'[^0-9]', '', start))
        if 'PM' in start:
            startNum += 12
        total += 18 - startNum

        endNum = int(re.sub(r'[^0-9]', '', end))
        if 'PM' in endNum:
            endNum += 12
        total += endNum - 13
        print(total)