def wordSalad(a,b,c,d):
    return('I love ' + a + ' and ' + b + ' with ' + c + ' and ' + d +'.')
#print(wordSalad('Paige','Hannah','Panera','Taco Bell'))


def distTravel(a,t):
    return((1/2)*0.3*a*t**2)
    #print(distTravel(2,4))


def excelPrep(myStr):
    x = myStr.count('$')
    myStr = myStr.replace('$','')
    myStr = myStr.lower()
    return (myStr,x)
#print(excelPrep('=SUM($A$4:$A$12)'))
