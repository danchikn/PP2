def histogram(x):
    for i in range(0, len(x)):
        for j in range(0, x[i]):
            print('*', end="")
        print()
histogram([4,9,7])