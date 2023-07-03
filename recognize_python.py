
num1 = 42 #variable declaration
num2 = 2.3 #float value
boolean = True #primitive data type-boolean
string = 'Hello World' #primitive data type-string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #composit data type-list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #composite data type-dictionary
fruit = ('blueberry', 'strawberry', 'banana') #composite data type- tupule
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log the second value in the list
pizza_toppings.append('Mushrooms') #add muschrooms to the list
print(person['name']) #log the value of the name key
person['name'] = 'George'# change value of name key
person['eye_color'] = 'blue' #add value in dictionary
print(fruit[2]) #access third value of tuple

if num1 > 45:              #conditional if else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!") #conditional else if
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop stop at 4
    print(x)
for x in range(2,5): #for loop start, stop
    print(x)
for x in range(2,10,3): # start, stop, increment
    print(x)
x = 0
while(x < 5): # while statment
    print(x)
    x += 1

pizza_toppings.pop() #remove last 
pizza_toppings.pop(1) # return the value at index 1

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)