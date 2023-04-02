def solve(numheads, numlegs):
    rabbits = 0.5 * numlegs - numheads
    chickens = 2 * numheads - 0.5 * numlegs
    return (rabbits, chickens)

numheads = int(input())
numlegs = int(input())
onc = solve(numheads, numlegs)

print(onc)