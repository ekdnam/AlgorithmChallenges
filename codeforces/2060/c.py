# https://codeforces.com/contest/2060/problem/C

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    lo, hi = 0, n - 1
    res = 0
    while lo < hi:
        curr_sum = arr[lo] + arr[hi]
        if  curr_sum == k:
            lo += 1
            hi -= 1
            res += 1
        elif curr_sum < k: 
            lo += 1
        else:
            hi -= 1
    answers.append(res)

answers = []
t = int(input())
for _ in range(t):
    solve()
print("\n".join(map(str, answers)))