s=input().split('+')
d = {
    'ONE': '1',
    'TWO': '2',
    'THR': '3',
    'FOU': '4',
    'FIV': '5',
    'SIX': '6',
    'SEV': '7',
    'EIG': '8',
    'NIN': '9',
    'ZER': '0'
}
d2 = {
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THR',
    '4': 'FOU',
    '5': 'FIV',
    '6': 'SIX',
    '7': 'SEV',
    '8': 'EIG',
    '9': 'NIN',
    '0': 'ZER'
}
e=0
for i in range(len(s)):
    f=""
    for j in range(len(s[i])):
        if s[i][j:j+3] in d:
            f=f+d[s[i][j:j+3]] 
    e=e+int(f)
n=e
k=0
a=""
while n!=0:
    k=k+1
    n=n//10
for i in range(k):
    if str(e%10) in d2:
        a=d2[str(e%10)]+a
        e=e//10
print(a)