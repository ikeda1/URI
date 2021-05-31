while(True):
    stop = True
    nWagons = int(input())
    if nWagons == 0:
        break;

    while(stop):
        Wagons = list(map(int, input().split()))
        # wagon[i] = [int(x) for x in input().split()]
        if Wagons == [0]:
            print()
            stop = False;
            break;
        Station = []
        B = []
        Fail = False

        # Comeca verificacao
        while not Fail:
            currPos = 0
            while (not Fail):
                for i in range(1, nWagons+1, 1):
                    # print(f"i:{i} currPos:{Wagons[currPos]}")
                    if (i == Wagons[currPos]):
                        # print("went to B")
                        B.append(i)
                        currPos += 1
                        # if (len(Station) != 0):
                            # print(f"Station top: {Station[len(Station)-1]} currPos:{Wagons[currPos]}")

                        while (True):
                            if (len(Station) >= 1 and Station[len(Station)-1] == Wagons[currPos]):
                                B.append(Station.pop())
                                currPos += 1
                            else:
                                break;

                    else:
                        # print("went to station")
                        Station.append(i)

                # print("\nEstações")
                # print(f"Order:{Wagons}")
                # print(f"Station:{Station}")
                # print(f"B:{B}\n")

                if (len(Station) == 0):
                    print("Yes")
                else:
                    print("No")

                Fail = True
    