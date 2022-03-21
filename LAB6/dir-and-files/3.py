import os
path="LAB6/dir-and-files/text.txt"
if os.path.exists(path):
    d=path.split('/')
    print(d[len(d)-1])
