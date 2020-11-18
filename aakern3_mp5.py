def checkSum(myStr):
    ans = 0
    for letter in myStr:
        ans += ord (letter)

    ans = ans % 10
    return ans

#print(checkSum('cat'))

def sumNumbers(a,b,c):
    ans = 0
    al, bl, cl = [], [], []
    for i in range(a):
        al.append(a+i)
    for i in range(b):
        bl.append(b+i)
    for i in range(c):
        cl.append(c+i)
    for i in al + bl + cl:
        ans += i
    return ans

#print(sumNumbers(1,2,3))

def fileSum(fname):
    fn = open(fname,'r')
    ans = 0
    for line in fn:
        ans = ans + int(line)
    return ans

#print(fileSum('nums.txt'))
