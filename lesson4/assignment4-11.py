#รับจำนวนจริง x จาก input แล้วใช้วิธี bisection หาและแสดงค่าของรากที่ 3 ของ x
#กำหนดให้ a และ b มีค่าเกือบเท่ากัน เมื่อ |a-b| <= 10**-6 max(|a|,|b|)

#คำตอบ
x = float(input())  #รับค่าจำนวนจริง
L = 0; U = x  #กำหนดขอบซ้าย L = 0 และ ขอบขวา U = จำนวนจริงที่รับ x
r = (L + U)/2  #หาค่าตรงกลางของขอบซ้ายและวาหรือวิธี bisection 
r3 = r**3 
while abs(r3-x) > 1e-6*max(r3, x):
    if r3 > x:
        U = r
    else:
        L = r
    r = (L + U)/2
    r3 = r**3
print(r)