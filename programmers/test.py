

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}
S = "(A+B)*(C+D)"
for s in S:
    if s in prec:
        print(s)