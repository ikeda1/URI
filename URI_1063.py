def Insert(A, Station):
    Station.append(A.pop())
    return "I";

def Remove(Station, B):
    B.append(Station.pop())
    return "R";

while(True):
    answer = ""
    nWagons = int(input())
    if nWagons == 0:
        break;

    Wagons = list(map(str, input().split()))
    newWord = list(map(str, input().split()))
    A = []

    for i in range (nWagons-1, -1, -1):
        A.append(Wagons[i])

    B = []
    Station = []

    i = 0
    while(len(A) != 0):
        if (A[-1] == newWord[i]):
            answer += Insert(A, Station)
            answer += Remove(Station, B)
            i += 1
            while (True):
                if (len(Station) >= 1 and Station[-1] == newWord[i]):
                    answer += Remove(Station, B)
                    i += 1
                else:
                    break;
        else:
            answer += Insert(A, Station)
    
    if (B == newWord):
        print(answer)
    else:
        print(answer + " Impossible")