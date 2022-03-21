with open('LAB6/dir-and-files/input.txt','r') as f:
    text=f.read()
    with open('LAB6/dir-and-files/text.txt','w') as d:
        d.write(text)
