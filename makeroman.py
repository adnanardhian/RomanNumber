rome = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 ,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
rval = [1, 4,5,9, 10,40,50,90, 100, 400,500,900, 1000,4000]
def makeroman(n):
    if n==0:
        return n
    else:
        rm = ""
        i = -1
        while(n>0):
            i+=1
            if n<rval[i]:
                x = rval[i-1]
                rm=rm+rome.keys()[rome.values().index(x)]
                n = n-x
                i = -1
        return rm
