#เขียนคำสั่งตามที่แสดงใน comment เช่น ถ้าโจทย์ให้แสดงผลการเปรียบเทียบว่า a เป็น 0 หรือไม่ ก็เขียนคำสั่ง print(a == 0)
แสดงผลของการเปรียบเทียบว่า s เป็นสตริงที่ขึ้นต้นด้วยตัวอักษรอังกฤษตัวใหญ่ และลงท้ายด้วยตัวเลข

#คำตอบ
print("A" <= s[0] <= "Z" and "0" <= s[-1] <= "9")
