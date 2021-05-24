while(True):
    P, N, C, *rest = [int(x) for x in input().split()]
    count = 0
    answer = 0
    if N == 0 and P == 0 and C == 0:
        break;

    cbd = []
    for _ in range(N):
        x = list(map(int, input().split()))
        cbd.append(x)

    # j = lines     i = rows
    # A verificação dos palitos é feita na vertical
    for j in range (0, P):
        count = 0
        for i in range (0, N):
            if cbd[i][j] == 1:
                count += 1
            else:
                count = 0
                
            if count == C:
                answer += 1

    print(answer)