"""print("\tเลือกเมนูเพื่อทำรายการ")
print("\t############################################")
print("\t กด 1 เลือกเหมาจ่าย")
print("\t กด 2 เลือกจ่ายเพื่ม")
x=int(input(" "))
y=int(input("กรุณาเลือกระยะทาง : "))
if x==1:
    if y >= 25 :
        print("ค่าใช้จ่ายทั้งหมด 55 บาท")
    else :
        print("ค่าใช้จ่ายทั้งหมด 25 บาท")
else :
    if y >= 25 :
        print("ค่าใช้จ่ายทั้งหมด 80 บาท")
    else :
        print("ค่าใช้จ่ายทั้งหมด 25 บาท")

print("กรุณากรอกจำนวนครั้งการรับค่า")
x = int(input(""))
i=0
sum=0
while(i < x) : # while การทำ loop 
    number=int(input("กรอกตัวเลข"))
    i+=1
    sum = sum + number
print("ผลรวมค่าที่รับมาทั้งหมด : "+str(sum))"""

print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรเเกรม")
list=[]
i=1
x=0
z=1
while (True):
    x = input("อาหารโปรดอันดับที่ " + str(i) + "คือ :") # str = ตัวเลข
    list.append(x)
    i+=1
    if x == "exit" :
        print("\n อาหารสุดโปรดของคุณมีดังนี้")
        list.pop()
        break # หยุดการทำงาน
for x in list :
    print(str(z)+x,end="  ")
    z+=1