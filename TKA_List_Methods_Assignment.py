cars = ['bmw', 'mahindra', 'suzuki', 'rools royce', 'bentley', 'aston martin', 'tata', 'audi', 'mustang']

#Append
cars.append('ferrari')
print("Appended List: ", cars)

#Insert
cars.insert(3, 'porsche')
print("List Changed Using Insert Method: ", cars)

#Sort in ascending order
cars.sort()
print("Sorted List in Alphabetical Order: ", cars)

#Remove
cars.remove('audi')
print('List after removing audi: ', cars)

#Index
print("Index of Mustang is: ", cars.index('mustang'))
print('Index of Tata is: ', cars.index('tata'))

#Extend
l = ['tesla', 'nissan']
cars.extend(l)
print(cars)

#Pop
print("Last Element is: ", cars[-1])
cars.pop(-1)
print("After popping the last element: ", cars)

#Count
print('Count of BMW in list: ', cars.count('bmw'))

#Adding multiple elements to the list
l1 = ['jaguar', 'fiat']
cars.extend(l1)
print(cars)

#Insert multiple
cars[2:2] = ('volvo', 'honda')
print(cars)

#Sort in descending order
cars.sort(reverse = True)
print("List in  descending order: ", cars)

#Remove
cars.remove('bmw')
print('List after removing bmw: ', cars)

#Clear
cars.clear()
print(cars)


