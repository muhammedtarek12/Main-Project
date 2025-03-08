# while condition:
    ##
my_fruits = ['apple', 'orange', 'lemon', ['passion fruit', 'pineapple']]
for item in my_fruits: # apple, [''passion fruit', 'pineapple']
    if type(item) == list:
        for fruit in item:
            print(fruit.upper())
    else:
        print(item.upper()) # APPLE

x = 0
# while x < 10:
#     print(x)
#     # x = x + 2
#     x += 2

while True:
    if x == 10:
        break
    print(x) # 0 2 4 6 8
    x += 2

# my_number = input("Please enter a number: ")
#### Question
# you have a secret number 7
# 1) enter the game
# 2) ask the question
# 3) check the condition
# 4) take action or not
# winning_number = 7
# while True:
#     entered_number = int(input('Please enter a number: ')) # 6
#     if winning_number == entered_number: # 6 ==7?
#         print("Congrats, You won!")
#         break
#     print("Try again, you entered a wrong number")     #

# while True:
#     try:
#         num = int(input("Guess the number: "))
#         if num == 7:
#             print("Congratulations! You guessed it.")
#             break
#         else:
#             print("Wrong guess, try again!")
#     except ValueError:
#         print("Please enter a valid number.")
#################################################
print(sum([2, 6, 3, 5, 9, 8]))
##################
my_numbers = [2, 6, 3, 5, 9, 8]
total = 0
for num in my_numbers:
    # total = total + num # 0 + 2 -> 2, 2 + 6 -> 8
    total += num
print("sum of numbers:", total)

#################
def my_function():
    pass
# static func
def get_sum(): # function definition
    num_1 = 2
    num_2 = 3
    sum_num = num_1 + num_2
    return sum_num

print(get_sum()) # call
#########################################
# dynamic ( accepts variables as paramters)
def get_sum(num_1=2, num_2=2): # function definition
    sum_num = num_1 + num_2
    return sum_num

print(get_sum(2, 3)) # positional argument
print(get_sum(num_1=2, num_2=5)) # keyword argument
print(get_sum(num_2=13, num_1=1))
# print(get_sum(num=13, 1)) # Error
print(get_sum(1, num_2=99))
######################################################
numbers = [1, 23, 4, 55]

def get_sum_list(numbers):
    total = 0
    for num in numbers: # 1, 23, 4, 55
        if num % 2 == 1:
            total += num # 1, 23 -> 24, 55 + 24 -> 79
    return total

print(get_sum_list(numbers))

# 3 % 2 -> 1 # odd number -> 3
# 4 % 2 -> 0 # even number -> 4

def get_sum_list(*numbers):
    print("TYPE OF NUMBERS:", type(numbers))
    total = 0
    for num in numbers: # 1, 23, 4, 55
        if (type(num) == int) and (num % 2 == 1): # taking odd values and int types
            total += num # 1, 23 -> 24, 55 + 24 -> 79
    return total

print(get_sum_list(1, 2, 3, 4, 7, 8, 'apple'))
##########################
#checking for multiple types like: float, int
def get_sum_list(*numbers):
    print("TYPE OF NUMBERS:", type(numbers))
    total = 0
    for num in numbers: # 1, 23, 4, 55
        if (type(num) in [int, float]): # taking odd values and int types
            total += num # 1, 23 -> 24, 55 + 24 -> 79
    return total
print(get_sum_list(1, 2, 3, 4.5, 7, 8, 'apple'))
##########################
def greet_person(name):
    return f"Good Morning {name}"

print(greet_person('Ahmed'))

