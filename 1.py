a=input()

def sum(a):
    b=0
    if a=="": return "Oh, no!"
    for i in a:
        b=b+ord(i)
    if b<300: return "Oh, no!"
    return "It is tasty!"

sum(a)
