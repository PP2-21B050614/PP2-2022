a=""
for i in range(26):
    a="LAB6/dir-and-files/"+chr(65+i)+".txt"
    d=str(i)
    print(a)
    with open(a ,'x') as f:
        f.write(d)
