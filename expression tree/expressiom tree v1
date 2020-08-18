class Stack():
    stack_list = []

    def __str__(self):
        return self.stack_list

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        try:
            return_value = self.stack_list.pop()
            return return_value
        except IndexError:
            raise IndexError("Stack index error")

    def is_empty(self):
        return self.stack_list == []

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[len(self.stack_list) - 1]


class Operator():
    def __init__(self, express):
        self.express = express  #ค่าที่รับเข้ามา
        print("test",self.express) ###################################
        self.postfix = []
        self.__to_posfix()

    def __to_posfix(self):
        mystack = Stack()  ###เรียกใช้function_Stack
        prec = {'(': 0, '!': 1, '&': 2, '+': 3}
        operator_list = ['(', '!', '&', '+', ')']
        InfixGET = self.express  #เก็บค่าที่inputเข้ามา
        print('tokenlist',InfixGET)
        bracket_flag = False
        value = ""
        for CharInInfixGET in InfixGET:
            if CharInInfixGET not in operator_list:
                value += CharInInfixGET  #I 1 => I1
            elif CharInInfixGET in operator_list:
                if value != "":
                    self.postfix.append(value)   #ใส่I1เข้าไปในpostfix
                    value = ""       #set temp_charเป็น''
                    #print(mystack)
                    while mystack.peek() == '!':      #peekจากคลาสstack
                        self.postfix.append(mystack.pop())
                if CharInInfixGET == '(':
                    if mystack.peek() == '!':  #peekจากคลาสstack
                        bracket_flag = True
                    mystack.push(CharInInfixGET)  #จากคลาสstack
                elif CharInInfixGET == '!':
                    mystack.push(CharInInfixGET)  #จากคลาสstack
                elif CharInInfixGET == ')':
                    topToken = mystack.pop()
                    while topToken != '(':
                        self.postfix.append(topToken)
                        topToken = mystack.pop()
                    if bracket_flag == True and mystack.peek() == '!':
                        self.postfix.append(mystack.pop())
                        bracket_flag = False
                else:
                    while (not mystack.is_empty()) and (prec[mystack.peek()] >= prec[CharInInfixGET]):
                        self.postfix.append(mystack.pop())
                    mystack.push(CharInInfixGET)
        if value != "":
            self.postfix.append(value)
        while not mystack.is_empty():
            self.postfix.append(mystack.pop())
        print(''.join([str(elem) for elem in self.postfix]))   #เรียงลำดับแบบpostfix
        print(self.postfix)     #แปลงป็นpostfix

    def get(self):
        return self.postfix

Operator('(((I0&I1&!I2)+!I1)+I3)')


