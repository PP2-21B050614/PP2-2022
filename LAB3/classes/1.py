class getprint:
    n=""
    def getString(par):
        n=input()
        par.n = n
    def printString(par):
        print(par.n)

d = getprint()
d.getString()
d.printString()
