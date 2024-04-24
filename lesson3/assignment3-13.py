#มีตัวแปร month เก็บสตริงอยู่แล้ว ถ้า month เก็บชื่อเดือน ให้แสดง Yes ไม่เช่นนั้นก็แสดง No 
ชื่อเดือนมีดังนี้ January, February, March, April, May, June, July, August, September, October, November, December

#คำตอบ
m = ["January", "February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"]
if month in m:
    print("yes")
else:
    print("no")
