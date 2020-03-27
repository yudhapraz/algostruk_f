A = [3,7,34,38,56,78,89,190]
B = [4,5,6,12,23,36,43,64,76,120]

def sortToC(a, b):
    c = a+b
    for i in range(1, len(c)):
        nilai = c[i]
        pos = i
        while pos > 0 and nilai < c[pos - 1]:
            c[pos] = c[pos-1]
            pos -=1
        c[pos] = nilai
    return c


