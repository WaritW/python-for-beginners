#รับจำนวนจริง a,b และ e จาก input (ในบรรทัดเดียวกัน คั่นด้วยช่องว่าง) แล้วแสดงคำว่า close enough ถ้า |a-b| <= e*max(|a|,|b|) เป็นจริง ไม่เช่นนั้น แสดงว่า not equal

#คำตอบ
x = input().split()
a = float(x[0])
b = float(x[1])
e = float(x[2])
if abs(a-b) <= e * max(abs(a),abs(b)):
    print("close enough")
else:
    print("not equal")
