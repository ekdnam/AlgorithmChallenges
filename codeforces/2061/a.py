def solve():
    import sys

    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])

    index = 1
    answers = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index : index + n]))
        index += n

        # Count even and odd numbers
        E = sum(1 for x in arr if x % 2 == 0)
        O = n - E  # number of odd numbers

        if E == 0:
            # All odd
            # If n=1, answer is 0; else it's n-1
            # (n=1 => no points, n>1 => we can score on all except the first operation)
            if n == 1:
                answers.append(0)
            else:
                answers.append(n - 1)
        else:
            # We have at least one even number
            # 1 point from the first operation (using an even)
            # plus min(O, n-1) from the remaining operations
            answers.append(1 + min(O, n - 1))

    print("\n".join(map(str, answers)))


solve()
