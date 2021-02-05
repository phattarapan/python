listshop=[0,0,0,0,0]
cost=[80,100,60,45,25]
def menu():
    global choice
    print('โปรเเกรมร้านเครื่องเขียนออนไลน์\n 1. แสดงรายการสินค้า\n 2. หยิบสินค้าในตะกร้า\n 3. แสดงรายจำนวนและราคาสินค้าที่หยิบ\n 4. หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม ')
    choice = input('กรุณาเลือกทำรายการ : ')

def costmenu():
    print('\tรายการสินค้า')
    print('-'*30)
    print('1.รูปวาด     ราคา  80 บาท')
    print('2.พวงกุญเเจ  ราคา 100 บาท')
    print('3.สมุดโน๊ต    ราคา 60 บาท')
    print('4.การ์ด      ราคา  45 บาท')
    print('5.ปากกา     ราคา  25 บาท')
    print('-'*30)
    
def pickmenu():
    global pick
    print('\t1.รูปวาด')
    print('\t2.พวงกุญเเจ')
    print('\t3.สมุดโน๊ต')
    print('\t4.การ์ด')
    print('\t5.ปากกา')
    print('\t6.ออกจากหน้านี้')
    prick = (input('เลือกหยิบสินค้าหมายเลข  :'))
    print('')

    if pick  == 1:
        listshop[0] += 1
    elif pick == 2:
        listshop[1] += 1
    elif pick == 3:
        listshop[2] += 1
    elif pick == 4:
        listshop[3] += 1
    elif pick == 5:
        listshop[4] += 1
    elif pick == 6:
    break 
    
def allpick():
    list_fruit = ['รูปวาด','พวงกุญเเจ','สมุดโน๊ต','การ์ด','ปากกา']
    list_cost =[80,100,60,45,25]
    print("{0:-<10}{1:-<10}{2:-<10}{3}".format('สินค้า','ราคา','จำนวน','ยอดรวม'))
    for i in range(0,5):
        print("{0:-<10}{1:-<10}{2:-<10}{3}".format(list_fruit[i], list_cost[i], listshop[i], listshop[i]*list_cost[i]))

def outpick():
    print('\t1.รูปวาด')
    print('\t2.พวงกุญเเจ')
    print('\t3.สมุดโน๊ต')
    print('\t4.การ์ด')
    print('\t5.ปากกา')
    print('\t6.ออกจากหน้านี้')
    outpick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ 6 เพื่อออก"))
    if outpick  == 1:
        listshop[0] -= 1
    elif outpick == 2:
        listshop[1] -= 1
    elif outpick == 3:
        listshop[2] -= 1
    elif outpick == 4:
        listshop[3] -= 1
    elif outpick == 5:
        listshop[4] -= 1

while True:
    menu()
    if choice == '1':
        costmenu()
    elif choice == '2':
        pickmenu()
    elif choice == '3':
        allpick()
    elif choice == '4':
        outpick()
    elif choice == '5':
        ch = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if ch == 'y':
            print('*'*30)
            print('\tThank you')
            print('*'*30)
            break
        elif ch == 'n':
            continue