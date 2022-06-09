students = { 'john':85, 'mark': 65, 'teddy': 72 }

for name,score in students.items():
    if score >= 80:
        print(name + ' A')
    elif score >= 70 and score < 80:
        print(name + ' B')
    elif score >= 60 and score < 70:
        print(name + ' C')
    elif score >= 50 and score < 60:
        print(name + ' D')
    else:
        print(name + ' F')
        
print("Complete !!")