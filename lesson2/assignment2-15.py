#เขียนคำสั่งตามที่แสดง
อ่านสตริงจาก input ที่มีรูปแบบ  
รหัสนักศึกษา: คะแนน, คะแนน, คะแนน เช่น 10232: 20, 30.5, 15.8

เก็บสตริงรหัสนักศึกษาใน student_id
เก็บคำนวนคะแนนเฉลี่ยใน average_point

#คำตอบ
a = input().split(": ")
student_id = a[0]
x = a[1].split(", ")
s = float(x[0])
s += float(x[1])
s += float(x[2])
average_point = s/3