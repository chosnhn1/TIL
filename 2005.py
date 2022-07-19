T = int(input())


stack = [0] * 11
stack[1] = [1]
stack[2] = [1, 1]
i = 3

# 1
# 1 1
# 1 2 1
# 1 3 3 1


while i < 11:
    l = len(stack[i-1]) + 1
    newline = [1] * (l)
    for k in range(1, l-1):
        newline[k] = stack[i-1][k-1] + stack[i-1][k]

    stack[i] = newline
    i += 1


for t in range(1, T+1):
    N = int(input())

    print(f'#{t}')
    for n in range(1, N+1):
        for i in stack[n]:
            print(i, end=" ")
        print()