a=input()
b=0
for i in a:
    b=b+ord(i)
if b<300:
    print("Oh, no!")
else:
    print("It is tasty!")