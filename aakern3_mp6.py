def cardType(myCard):
    if not myCard.isdigit():
        return 'Invalid'
    x = len(myCard)
    if x > 16 or x < 16:
        return('Invalid')
    if int(myCard[0]) == 4:
        return('Visa')
    if int(myCard[0]) == 5:
        return('Mastercard')
    if int(myCard[0]) == 6:
        return('Discover Card')
    else:
        return('Unknown')

#print(cardType('43195845771k3854'))


def voteComp(x,y,z):
    if int(x) == int(y):
        return x
    if int(y) == int(z):
        return y
    if int(z) == int(x):
        return z
    else:
        return 'ERROR'
#print(voteComp(34,45,34))

def phoneCheck(number):
    if number[0] == '(' or number[0:2] == '+1' or ord(number[0]) >= 48 and ord(number[0]) <= 57:
        
        for character in ['.',' ','(',')','-']:
            number = number.replace(character,"")
        if number[0:2] == '+1':
            number = number[2:]
        if len(number) >10 or len(number) < 10:
            return 'Invalid'
        if not number.isdigit():
            return 'Invalid'
        else:
            return 'Valid'
    else:
        return 'Invalid'

#print(phoneCheck('+1(913)382-9842'))

    
        
    


    
    
