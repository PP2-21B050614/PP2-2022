def solve(numheads, numlegs):
    rab=int((numlegs-2*numheads)/2)
    chick=int(numheads-rab)
    print(rab,chick)

head, leg= int(input()), int(input())
solve(head,leg)