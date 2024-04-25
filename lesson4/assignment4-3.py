#เขียนโปรแกรมตามผังงาน

#คำตอบ
c = 0
while n > 0:
    n = n - 1
    if n%3 == 0:
        n = n - c
        c += 1
print(c)