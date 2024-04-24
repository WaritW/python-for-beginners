#เขียนโปรแกรมตามผังงาน

#คำตอบ
a = int(input())
b = int(input())
if a < b:
  min = a
  max = b
else:
  min = b
  max = a
print(min, max)