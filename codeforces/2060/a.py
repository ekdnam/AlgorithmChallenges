# https://codeforces.com/contest/2060/problem/A
def solve():
    import sys

    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])

    index = 1
    answers = []
    n = 4
    while t:
        t -= 1
        arr = list(map(int, input_data[index : index + n]))
        index += n

        res = 1
        # a2 = a0 + a1
        curr = 1
        a3 = arr[0] + arr[1]
        if arr[1] + a3 == arr[2]:
            curr += 1
        if arr[2] + a3 == arr[3]:
            curr += 1
        res = max(res, curr)

        # a3 = a2 - a1
        curr = 1
        a3 = arr[2] - arr[1]
        if a3 + arr[2] == arr[3]:
            curr += 1
        res = max(res, curr)

        answers.append(res)

    print("\n".join(map(str, answers)))


solve()
