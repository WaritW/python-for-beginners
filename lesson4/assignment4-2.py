#เขียนโปรแกรมตามผังงาน

#คำตอบ
n = len(b)
d = 0
k = 0
while k < n:
    d += (2**k)(int(b[n-k-1]))
    k += 1
print(d)