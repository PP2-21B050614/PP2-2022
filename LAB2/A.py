ls = input().split()

mx = 0
for i in range(len(ls)):
  mx = max(i + int(ls[i]), mx)
  if mx <= i and i != len(ls)-1:
    print(0)
    break
else:
  print(1)