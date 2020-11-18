def spliceString( x,y,z ):
    return(x[z]+y[z:])
#print(spliceString('Caitlen', 'The Builder', 3))

def wheatChess(n):
    x=0
    for a in range(n):
        x = 2**a + x
    return x
#print(wheatChess(64))


def strangeMath(x,y,z):
    return (int(x)+ round(y))%z
#print(strangeMath(3.6,3.2,4))
    
