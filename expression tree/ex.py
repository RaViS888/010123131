def make_array(origin):
    n = 0
    for i in origin:
        if i in '0123456789' or i in '+-*/': #นับจำนวนตัวเลขหรือเครื่องหมาย
            n += 1
    A = ['None']
    i = 0
    while n > 2**i: #จำนวนที่ node ของ complete binary tree มากกว่าสิ่งที่ต้องใส่ไป
        i += 1
        temp = (2**i)-1

    return A*temp
    
#####################################

def binary_tree_expression(origin, array):
    #
    origin_slide = origin[1:-1] #จะไม่นับวงเล็บนอกสุด    (ตังแต่ตัวที่1 ถึงตัวก่อนสุดท้าย)
    q = 0  #q คือ parents ตอนแรกตั้งไว้ที่ตำแหน่ง 0
    for i in origin_slide:
        pl = (2*q)+1 #ลูกทางซ้าย
        pr = (2*q)+2 #ลูกทางขวา
        if i == '(':
            if array[pl] == 'None': #ถ้าเจอ"("จะเปลี่ยนำแหน่ง parents ไปเป็นลูกทางซ้ายของต่ำแหน่ง parents เดิมโดยที่ทางขวายังเป็น None อยู่
                q = pl
            else:                   #แต่ถ้ามีตัวเลขหรือเครื่องหมายจะเปลี่ยนต่ำแหน่ง parents ไปเป็นลูกทางขวาของต่ำแหน่ง parent เดิม
                q = pr       
        elif i in '0123456789':
            if array[pl] in '0123456789' or array[pl] in '+-*/': #แต่ถ้ามีตัวเลขหรือตัวเครื่องหมายในลูกทางซ้ายจะให้เป็นลูกทางขวา
                array[pr] = i
            else:               #ถ้าเจอตัวเลขจะให้เป็นลูกทางซ้าย
                array[pl] = i
        elif i in '+-*/': #ถ้าเจอเครื่องหมายจะให้เป็น parents เลย
            array[q] = i
        elif i == ')': #ถ้าเจอ')'จะตรวจว่าต่ำแหน่งของ parents เป็นทางซ้ายหรือขวาเพื่อที่จะย้อนกลับไปหา ปู่(parents ของ parents ตัวนั่น)
            if q%2 == 1: #ถ้าต่ำแหน่งของ parents เป็น คี่แสดงว่าเป็นทางซ้ายของปู่
                q = int((q-1)/2)
            elif q%2 == 0: #ถ้าต่ำแหน่งของ parents เป็น คู่แสดงว่าเป็นทางซ้ายของปู่
                q = int((q-2)/2)

    return array
#------------------------------------------------------------------------------------

def main_1(string):
    array = make_array(string)
    array_tree = binary_tree_expression(string, array)
    return array_tree
    
array_tree = main_1('(3+(4*5))')
print(array_tree)
