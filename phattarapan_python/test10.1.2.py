dictionary = []
word_type = []
meaning = []
def menu():
    global choice
    print('\nพจนานุกรม')
    print(' 1. เพิ่มคำศัพท์\n 2. แสดงคำศัพท์\n 3. ลบคำศัพท์\n 4. ออกจากโปรเเกรม')
    choice = (input('กรุณาเลอกทำรายการ :'))

def puss():
    dictionary.insert(0,input('\nเพิ่มคำศัพท์ :'))
    word_type.insert(0,input('ชนิดคำศัพท์ (n. ,v. ,adj. ,adv. :)'))
    meaning.insert(0,input('ความหมาย :'))
    print('*****เพิ่มคพศัพท์เรียนร้อย*****')

def show():
    print('-'*20)
    print('คำศัพท์มีทั้งหมด',len(dictionary))
    print('-'*20)
    x = 0
    while x < len(dictionary) :
        print(dictionary[x],' ',word_type[x],' ',meaning[x])
        x = x+1

def delete():
    x = str(input('\nพิมพ์คำศัพท์ที่ต้องการลบ :'))
    x2 = str(input('ต้องการลบ' +x+ 'ใช่หรือไม่ y/n :'))
    if x2 == 'y' :
        z=0
        while z < len(dictionary):
            if x == dictionary[z]:
                del word_type[z]
                del meaning[z]
            z = z+1
        dictionary.remove(x)
        print('*****ลบ' +x+ 'เรียบร้อยเเล้ว*****')
    else:
        print('*****ยกเลิกกสนลบคำศัพท์*****')

while True:
    menu()
    if choice == '1':
        puss()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    else:
        o = str(input('ต้องการออกจากโปรเเกรมใช่หรือไม่ y/n :'))
        if o == 'y':
            print('\n*****ออกจากโปรเเกรมเรียนร้อยเเล้ว*****')
            break
        else:
            continue