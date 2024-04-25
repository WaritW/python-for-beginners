#อ่านสตริง t จาก input เพื่อนับและแสดงว่ามีสระใน t กี่ตัว (นับทั้งตัวเล็กและตัวใหญ่ โดยใช้วงวน while) เช่น Anna มีสระเป็นจำนวน 2 ตัว แบบฝึกหัดของบทก่อน เราจำกัดขนาดของ t แค่ 5 ตัวอักษร แล้วก็ยังไม่ได้เรียนเรื่องวงวน ก็เขียนเป็นคำสั่งได้ดังข้างล่างนี้ จะเห็นว่ามีคำสั่งที่ทำงานในรูปแบบซ้ำ ๆ กัน ก็นำมาทำในวงวนได้

            t = input()
            c = 0
            vowels = "aeiouAEIOU"
            if t[0] in vowels:
                c += 1
            if t[1] in vowels:
                c += 1
            if t[2] in vowels:
                c += 1
            if t[3] in vowels:
                c += 1
            if t[4] in vowels:
               c += 1
            print(c)

#คำตอบ
t = input()
c = 0
vowels = "aeiouAEIOU"
k = 0
while k < len(t):
    if t[k] in vowels:
        c += 1
    k += 1
print(c)