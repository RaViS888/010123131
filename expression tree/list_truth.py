#6101012620130
import itertools
class Stack:  # ref form https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
    stack_list = []  # เก็บoperator symbol

    def __str__(self):
        self.stack_list

    def is_empty(self):  # ทำให้stackว่าง
        return self.stack_list == []

    def push(self, item):
        self.stack_list.append(item)  # เพิ่มเข้า stack

    def pop(self):
        return self.stack_list.pop()  # สงค่าท้าย และลบค่านั้นออก

    def peek(self):  # ดู stack ที่เก็บไว้(ใช้ตรวขว่าเป็น!)ถ้าไม่มีreturn none ถ้ามีให้ return ค่าตัวก่อนหน้า
        if self.stack_list == []:  # ดูว่าในstack ว่างเปล่าหรือไม่
            return None
        else:
            return self.stack_list[len(self.stack_list) - 1]


class Infix_to_post:
    def __init__(self, express):
        self.express = express  # ค่าที่รับเข้ามา
        self.postfix = []
        self.__to_posfix()
        # print("input=>", express)

    def __to_posfix(self):
        mystack = Stack()  # เรียกใช้function_Stack
        prec = {'(': 0, '!': 1, '&': 2, '+': 3}  #check ความสำคัญ
        operator_sym = '()!&+'  # () AND OR NOT
        # print(operator_sym)
        InfixGET = self.express  # เก็บค่าที่inputเข้ามา
        self.char_val = []
        check_not = ''   #
        char_keep = ""

        for CharInInfixGET in InfixGET:
            if CharInInfixGET not in operator_sym:
                char_keep += CharInInfixGET  # I 1 => I1
            elif CharInInfixGET in operator_sym:
                #print(CharInInfixGET)
                if char_keep != "":
                    self.postfix.append(char_keep)  # ใส่I1 append ใน postfix
                    if char_keep not in self.char_val:
                        self.char_val.append(char_keep)
                    char_keep = ""  # set temp_char เป็น''
                    # print(mystack)
                    # print(mystack.peek())
                    while mystack.peek() == '!':  # peekจากคลาสstack
                        self.postfix.append(mystack.pop())
                if CharInInfixGET == '(':  # ถ้าเจอ ( ให้ดูตัวก่อนหน้าถ้าเป็น !
                    if mystack.peek() == '!':
                        check_not = True
                    mystack.push(CharInInfixGET)  # เพิ่มเข้าmytack
                elif CharInInfixGET == '!':
                    mystack.push(CharInInfixGET)  # เพิ่มเข้าmytack
                elif CharInInfixGET == ')':
                    topToken = mystack.pop()  # ให้ topToken = operator symbol ตัวท้ายที่อยู่ใน list ของ stack
                    while topToken != '(':
                        self.postfix.append(topToken)
                        topToken = mystack.pop()  # ตรวจดู (
                    if check_not == True and mystack.peek() == '!':
                        self.postfix.append(mystack.pop())
                        check_not = False
                else:
                    while (not mystack.is_empty()) and (prec[mystack.peek()] >= prec[CharInInfixGET]):
                        self.postfix.append(mystack.pop())
                    mystack.push(CharInInfixGET)
        if char_keep != "":
            self.postfix.append(char_keep)
        while not mystack.is_empty():
            self.postfix.append(mystack.pop())
        # print(''.join([str(elem) for elem in self.postfix]))  # เรียงลำดับแบบpostfix
        print("input=>", self.express)
        #print(self.char_val)
        
        #print(len(self.char_val))
        N = self.char_val
        n = len(N)
        table = list(itertools.product(['0', '1'], repeat=n))
        print(N)
        for j in range(len(table)):
            print(table[j])

        print(self.postfix)  # แปลงป็นpostfix
        print("---------------------------------------")

    def get(self):  # ค่าที่แปลงเป็น postfixแล้ว
        return self.postfix

Infix_to_post("!(1+0)")
Infix_to_post("!(!(0+I0&1))")
Infix_to_post("(I0+!I1+!(I2))&(!I0+I1+I2)")
Infix_to_post("!(I0&I1)+!(I1+I2)")
Infix_to_post("(((I0&I1&!I2)+!I1)+I3)")
