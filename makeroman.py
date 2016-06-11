rome = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
rval = [1, 5, 10, 50, 100, 500, 1000,4000]
def makeroman(n):
    if n==0:
        return n
    if n in rome.values():
        return rome.keys()[rome.values().index(n)]
    else:
        rm = ""
        x = 0
        i = -1
        while(n>0):
            i+=1
            if n<rval[i]:
                if (n==4 or n==9):
                    y=n+1
                    rm+="I"
                    rm+=rome.keys()[rome.values().index(y)]
                    break
                elif ((n>=40 and n<50) or (n>=90 and n<100)):
                    y=n+10-(n%10)
                    rm+="X"
                    rm+=rome.keys()[rome.values().index(y)]
                    n = n - 10*(n/10)
                    i=-1
                elif ((n>=400 and n<500) or (n>=900 and n<1000)):
                    y=n+100-(n%100)
                    rm+="C"
                    rm+=rome.keys()[rome.values().index(y)]
                    n = n - 100*(n/100)
                    i=-1
                else:
                    x = rval[i-1]
                    rm=rm+rome.keys()[rome.values().index(x)]
                    n = n-x
                    i = -1
        return rm
