#เขียนโปรแกรมตามผังงานข้าง ๆ นี้ (มีตัวแปร a ให้แล้ว ไม่ต้องตั้งค่าหรือรับอินพุตใด ๆ)

#คำตอบ
if a%2 == 0:
    a *= 2
else:
    if a > 10:
        a //= 2
    else:
        a = 0
print(a)