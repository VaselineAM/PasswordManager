import random
def PASSWORDGENERATOR():
    capitalletters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["!","@","#","$","%","^","&","*","?"]
    #password = [capitalletters,numbers,symbols]
    pwdgen = ""

    #getting the symbols
    for x in range(random.randint(2,4)):
        symbolrandom = random.randint(0,len(symbols)-1)
        pwdgen = pwdgen + symbols[symbolrandom]
    #getting the numbers
    for x in range(random.randint(2,4)):
        numberandom = random.randint(0,len(numbers)-1)
        pwdgen = pwdgen + numbers[numberandom]
    #getting the alphabets
    for x in range(random.randint(2,4)):
        letterrandom = random.randint(0,25)
        capitalorlower = random.randint(0,1)
        if capitalorlower==0: #if capitalorlower=0, letter is lower case
            pwdgen = pwdgen + capitalletters[letterrandom].lower()
        else:
            pwdgen = pwdgen + capitalletters[letterrandom]

    pwd = ""
    pwdgenlist = list(pwdgen)
    random.shuffle(pwdgenlist)
    #print(pwdgenlist)
    for x in range(len(pwdgenlist)):
        pwd = pwd + pwdgenlist[x]
    return pwd

    #print(''.join(pwdgenlist))

PASSWORDGENERATOR()