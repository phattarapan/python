order_list = []
def menu():
    print(' ')
    print('*****โปรเเกรมร้านเครื่องเขียนออนไลน์*****\n 1. เเสดงรายการสินค้า\n 2. เลือกสินค้า\n 3. เเสดงรายการสินค้าที่เลือก\n 4. ปิดโปรเเกรม')

def preview():
    print('\tรายการสินค้า')
    print('-'*30)
    print('1.รูปวาด     ราคา  80 บาท')
    print('2.พวงกุญเเจ  ราคา 100 บาท')
    print('3.สมุดโน๊ต    ราคา 60 บาท')
    print('4.การ์ด      ราคา  45 บาท')
    print('5.ปากกา     ราคา  25 บาท')
    print('-'*30)
    
def prick():
    while (True):
        print('\t1.รูปวาด')
        print('\t2.พวงกุญเเจ')
        print('\t3.สมุดโน๊ต')
        print('\t4.การ์ด')
        print('\t5.ปากกา')
        print('\t6.ออกจากหน้านี้')
        prick = (input('เลือกหยิบสินค้าหมายเลข  :'))
        print('')
        try:
            if int(prick)==1 or prick=='1':
                order_list.append('รูปวาด')
            elif int(prick)==2 or prick=='2':
                order_list.append('พวงกุญเเจ')
            elif int(prick)==3 or prick=='3':
                order_list.append('สมุดโน๊ต')
            elif int(prick)==4 or prick=='4':
                order_list.append('การ์ด')
            elif int(prick)==5 or prick=='5':
                order_list.append('ปากกา')
            elif int(prick)==6 or prick=='6':
                break
            else:
                print('กรุณากรอกหมายเลขให้ถูกต้อง') 
        except:
            print('กรุณากรอกหมายเลขให้ถูกต้อง')

def preorder():
    list_order = ['รูปวาด','พวงกุญเเจ','สมุดโน๊ต','การ์ด','ปากกา']
    list_price = [80,100,60,45,25]
    list_amount = [0,0,0,0,0]
    print('')
    print('-'*10+ 'สินค้าที่คุณได้หยิบไปมีดังนี้'+'-'*10)
    print('{0:-<13}{1:-<13}{2:-<13}'.format('สินค้า','ราคา','จำนวน',))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}'.format(list_order[i],list_price[i],list_amount[i]))


while (True):
    menu()
    a = int(input('กรุณาเลือกทำรายการ :'))
    if a == 1:
        preview()
    elif a == 2:
        prick()
    elif a == 3:
        preorder()
    elif a == 4:
        a = input('ต้องการออกจากโปรเเกรมใช่หรือไม่ y/n :')
        if a == 'y':
            print('*'*30)
            print('\tThank you')
            print('*'*30)
            break
        elif a == 'n':
            continue
        