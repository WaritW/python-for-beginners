#อ่านจำนวนเต็ม a, b และ c จาก input แล้วแสดงจำนวนเต็มที่มีค่า a, a+c, a+2c, ... บรรทัดละหนึ่งค่า โดยจะหยุดแสดงเมื่อค่าที่คำนวณมากกว่าหรือเท่ากับ b เช่น a=2, b=7, c=2 จะแสดง 2, 4 และ 6 บรรทัดละค่า

#คำตอบ 
x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
for i in range(a, b, c):
    print(i)