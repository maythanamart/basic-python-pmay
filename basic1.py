# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello Korn!")

text = "Hello May" #String
text = "Hello Mama" #String
# print(text)

# firstName = "Thanamart"
# lastName = "Sriaiemkul"
# print(firstName + ' ' + lastName)
# fullName = firstName + ' ' + lastName
# print(fullName)

number = 1 #int (Integer)
numberFloat = 1.5 #float, decimal

even = [2,4,6,8,10]
computer = ['cpu','ram','hdd','monitor','mouse','keyboard']
print(computer[1]) #ram
test = [2, 'cpu']
print(test)

bikes = [] #array, list
bikes.append('bike1') 
print(bikes) #bikes = ['bike1']
bikes.append('bike2')
print(bikes) #bikes = ['bike1', 'bike2']
bikes.append('bike3')
print(bikes) #bikes = ['bike1', 'bike2', 'bike3']

bikes[1] = 'bike4'
print(bikes)
bikes[1] = 'bike2'
print(bikes)

print(bikes[0])
print(bikes[1])
print(bikes[2])

# remove
bikes.remove('bike2')
print(bikes) #bikes = ['bike1', 'bike3']

# pop
bikes.pop()
print(bikes) #bikes = ['bike1']