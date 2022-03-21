list=["Arman","Bakdaulet","Kanat"]
s=""
for i in list:
    s=s+''+i+' '
print(s)
with open('C:\PP2/LAB6/dir-and-files/input1.txt','a') as f:
    f.write(s)