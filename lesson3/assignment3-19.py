#มีตัวแปร bmi เก็บจำนวนจริง จงเขียนคำสั่งให้แสดงข้อความตามค่าของ bmi ดังแสดงในตารางข้าง ๆ นี้ (ในที่นี้ bmi เก็บค่า body mass index ไม่เป็นจำนวนลบแน่ ๆ)

#คำตอบ
if bmi <= 15:
    msg = "Very severely underweight"
elif bmi <= 16:
    msg = "Severely underweight"
elif bmi <= 18.5:
    msg = "Underweight"
elif bmi <= 25:
    msg = "Normal"
elif bmi <= 30:
    msg = "Overweight"
else:
    msg = "Obese"
print(msg)