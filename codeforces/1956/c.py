# https://codeforces.com/contest/1956/problem/C

def solve():
    n = int(input())
    ans = 0
    for idx in range(1, n+1):
        ans += (2 * idx - 1) * idx
    print(f"{ans} {2*n}")
    ans = []
    for idx in range(n, 0, -1):
        curr = [1, idx]
        for jdx in range(1, n+1):
            curr.append(jdx)
        curr = " ".join(curr)
        ans.append(curr)
        curr = [2, idx]
        for jdx in range(1, n+1):
            curr.append(jdx)
        curr = " ".join(curr)
        ans.append(curr)
    print("\n".join(ans))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()