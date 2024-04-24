#มีตัวแปร text เก็บสตริงอยู่แล้ว อยากทราบว่าใน text มีตัวอักษรที่เป็นสระอะไรบ้าง (เฉพาะตัวเล็ก) เช่น Mission ให้แสดง io, understand ให้แสดง aeu (แสดงสระที่มี ตามลำดับตัวอักษร) ถ้าไม่มีสระเลยให้แสดง No vowels

#คำตอบ
r = ""
c = "a"
if c in text:
    r += c
c = "e"
if c in text:
    r += c
c = "i"
if c in text:
    r += c
c = "o"
if c in text:
    r += c
c = "u"
if c in text:
    r += c
if r == "":
    print("No vowels")
else:
    print(r)