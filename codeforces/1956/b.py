# https://codeforces.com/contest/1956/problem/B
def solve():
    n = int(input())
    seen = set()
    a = list(map(int, input().split(" ")))
    points = 0
    for ai in a:
        if ai in seen:
            points += 1
        seen.add(ai)
    print(points)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()