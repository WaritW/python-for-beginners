#เขียนโปรแกรมตามผังงาน

#คำตอบ
n = int(input())
s = 0
for i in range(1,n+1):
    if i%2 == 0:
        s += i
    s += i
print(s)