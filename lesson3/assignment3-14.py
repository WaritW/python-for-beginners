#เขียนโปรแกรมตามผังงาน

#คำตอบ
b = 1
if a < 0:
    a = -a
    b = 2*a
if not(a > 10):
    a *= 3
    b += a
print(a,b)