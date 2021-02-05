a=[]
while True :
    b = input("----ร้าน nooknick03_shop----\n เพิ่ม [a]\n เเสดง [s]\n ออกจากระบบ [x]\n")
    b = b.lower()
    if b=="a" :
        c = input("ป้อนรายการลูกค้า(ชื่อ:ลายเส้น:ขนาดภาพ)\n")
        a.append(c)
        print("\n *******ข้อมูลได้เข้าสู่ระบบเเล้ว*******\n")
    elif b == "s" :
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        print("{0:-<8}{1:-<10}{2:10}".format("ชื่อ","ลายเส้น","ขนาดภาพ"))
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        for d in a :
            e = d.split(":")
            print("{0[0]:<6}{0[1]:<10}{0[2]:<10}".format(e))
            continue
    elif b == "x" :
        c = input("ต้องการปิดโปรเเกรมใช่หรือไม่ y/n:")
        if c == "n" :
            print("ทำคำสั่งถัดไป")
        elif c == "y" :
            print("จบการทำงาน")
        break