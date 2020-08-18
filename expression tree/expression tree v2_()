from pythonds.basic import Stack

class ToPostfix():
    def __init__(self, expression):
        self.expression = expression
        self.postfix = []
        self.__to_posfix()

def infixToPostfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operator_list = ['(', '!', '&', '+', ')']
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    print('tokenlist',tokenList)
    char=''

    for token in tokenList:
        if token not in operator_list:
            char += token
        elif token in operator_list:
            postfixList.append(char)
            char=''
            if token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    print(postfixList)
    #print(postfixList)
    #print(postfixList[3])
    return " ".join(postfixList)  #==>ส่งเข้าpostpixlist


INSERT_INFIX="A1 * B + C * D"
#print(len(INSERT_INFIX)-INSERT_INFIX.count(' '))  #==>จำนวนnodeทั้งหมด
infixToPostfix(INSERT_INFIX)

#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
