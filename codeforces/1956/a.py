# https://codeforces.com/contest/1956/problem/A
def solve():
    k, q = (map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    q = list(map(int, input().split(" ")))
    answers = []
    for qi in (q):
        answers.append(str(min(qi, a[0] - 1)))
    print(" ".join(answers))

t = int(input())
for _ in range(t):
    solve()