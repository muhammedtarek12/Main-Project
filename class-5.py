
def get_square(*args): # arbitrary number of arguments
    # (5 ,7, 9, 10, 'apple')
    new_nums = []
    for num in args: # 1
        new_nums.append(num ** 2) # 1
    return new_nums # [1, 25, 49]

my_squared_list = get_square(1, 5 ,7) # None

print(get_square(1, 5 ,7))
print(get_square(1, 5 ,7, 9, 10, 11))


def get_personal_info(**kwargs): # arbitrary number of keyword arguments
    return f"{kwargs['first_name']} is my name. I have {kwargs['age']}. I'm a {kwargs['profession']}"

print(get_personal_info(first_name='Ahmed', age=30, profession='Engineer'))

#########
# operation = {'operator': '+'}
def calculator(*nums, **kwargs):
    if '+' in kwargs['operator']:
        addition = sum(nums)
    if '-' in kwargs['operator']:
        subtract = nums[0]
        for num in nums[1:]:
            subtract = subtract - num
    return addition, subtract

print(calculator(1, 2, operator=['+', '-'], name='mostafa'))

addition, subtraction = calculator(1, 2, operator=['+', '-'])
print(f"Addition result: {addition}, Subtraction result: {subtraction}")
##########################################################
names = ['ahmed', 'mahmoud', 'ali', 'amr', 'omar']
# dict -> {index: name}
names_dict = {}
for index, name in enumerate(names): # 0, 'ahmed', 1, 'mahmoud'
    names_dict[index] = name
print(names_dict)

def greet_user(name):
    return f"Hello {name}"

message = greet_user('Abdulrahman')
print(message)
#################

def get_amr(*names):
    for index, name in enumerate(names, start=1): # index, name
        if name.lower() == 'amr':
            return index
    return "Amr not found"

my_names = ['Mostafa', 'ahnmed', 'Khaled', 'Mahmoud']
# *names -> 'Mostafa', 'ahnmed', 'Khaled', 'Amr', 'Mahmoud'
print(get_amr(*my_names))

##################################
x = 2 # global variable
print(x) # 2
def add_numbers(): # definition
    global x # this is the outer x
    x = 5 # local variable
    y = 6
    return x + y

print(x) # 2 ,2

add_numbers()# function call

print(x) # 2, 5
#########################################
# input -> ['MOSTAFA', 'KhaleD', 'AMeer']
# output -> ['mostafa', 'khaled', 'ameer']

def get_lower_case(names):
    lower_case_names = []
    # print(names) # ('lamia', 'salma')
    for name in names:
        lower_case_names.append(name.lower())
    return lower_case_names

names_list = ['SALMA', "LAMIA", 'NOOR']

print(get_lower_case(names_list))

# list comprehension
lower_case_names = [name.lower() for name in names_list]
#################################################
countries_list = ['egypt', "libya", 'sudan']
countries = [country.title() for country in countries_list]
print(countries)
#############################################
countries_list = ['egypt', "libya", 'sudan', 'south africa']
# [operation loop condition]
countries_starts_with_s = [country.title() for country in countries_list if country.startswith('s')]
print(countries_starts_with_s)

#############################
countries_starts_with_s = []
for country in countries_list:
    if country.startswith('s'):
        countries_starts_with_s.append(country.title())
print(countries_starts_with_s)
##########################
def get_countires_starts_with_s(*countries):
    countries_starts_with_s = []
    for country in countries:
        if country.startswith('s'):
            countries_starts_with_s.append(country.title())
    return countries_starts_with_s

print(get_countires_starts_with_s('egypt', 'sudan', 'south korea'))
####################################################################
gender = 'male'
if gender == 'male':
    greeting_message = 'Hello Man'
else:
    greeting_message = 'Hello woman'
greeting_message = 'Hello Man' if gender == 'male' else 'Hello Woman'
#############################################################################
def addition(num1, num2):
    return num1 + num2

addition = lambda num1, num2: num1 + num2  # func_name = lambda parameters: operation

print(addition(2, 3))
##########################################
addition = lambda *nums: sum(nums)
print(addition(1, 2, 3))
####################################
get_lower = lambda name: name.upper()
my_list = ['mostafa', 'ahmed', 'mahmoud']
names_upper = list(map(get_lower, my_list)) # map(func, iterable)
print(names_upper)
#############################################
my_even_numbers = list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(my_even_numbers)