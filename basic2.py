pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']

while 'cat' in pets: #เข้า loop เมื่อ ยังมีแมวอยู่ใน list
    print("ยังมีแมวอยู่นะ")
    pets.remove('cat')
    
print("ไม่มีแมวแล้ว เย้")