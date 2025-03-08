profile = {
    'id': 1,
    'name': 'Ahmed',
    'address': 'Moattam'
}
profile_name = profile.get('name', 'Ahmed') # Ahmed
##
# profile_name = profile['name']
############################

# if condition:
# int('7.2') # str -> int
# float('2.5') # str -> float

# x = float(input('Please enter a number: ')) # 0.5
x = 0
if x <= 1:
    print(f"{x} is smaller than 1")
if 1 < x <= 10:
    print(f"{x} is between 1 and 10")
else:
    print(f"{x} is greater than or equal to 10")
####################################################

# grade = float(input("Please enter your grade: "))
grade = 0
if grade >= 90:
    student_grade = 'A'
elif grade < 90 and grade >= 80: #   80 <= grade < 90
    student_grade = 'B'
elif grade < 80 and grade >= 70:
    student_grade = 'C'
elif grade < 70 and grade >= 60:
    student_grade = 'D'
elif grade >= 0:
    student_grade = 'F'
else:
    student_grade = 'Invalid Input, please enter a number between 0 and 100'

print(student_grade)

####################################
# fruit = input("Please enter a fruit: ") # ='lemon cherry'
fruit = 'lemon,cherry'
my_fruits = fruit.split(',')

print("$$$$$$$$$$$$$$$$4", my_fruits)
my_list = ['apple', 'orange', 'cherry']

if fruit in my_list:
    print(f" {fruit} is present in the list")
else:
    my_list.append(fruit)

print("MY LIST: ", my_list)
###############################################
print('Mostafa'.count('o'))

if 'o' in 'Mostafa':
    pass
    # print("YESSS")

profile = {
    'id': 1,
    'name': 'Ahmed',
    'address': 'Moattam'
}

if 'name' in profile: # or profile.keys, to check for keys
    print("Yes yes")
else:
    print("NOOOO")

if 'Moatam' in profile.values():
    print("Yes yes")
else:
    print("NOOOO")
#######################################
is_student = True

if not is_student: # if not is_student ->  if is_student == False
    print("He is a student")
else:
    pass
######################################
# For LOOP
names_list = ['MOSTAFA', "AHMED", 'AMEER', 'KHALED']
# names_list[0] = names_list[0].lower()
name_lower = []
for name in names_list:
    # 1st loop: name = 'MOSTAFA', 2nd loop: name = 'AHMED'
    name = name.lower() # name = 'mostafa', name = 'ahmed'
    # name_lower.append(name) # 1st looop: [].append('mostafa'), 2nd loop: ['mostafa'].append('ahmed') -> ['mostafa', 'ahmed']
print(names_list)
##########################################
nums_list = [1, 2, 3, 4, 5]
for num in nums_list:
    pass
    # print(num)

for num in range(6): # start, stop, step range(6) -> [0, 1, 2, 3, 4, 5]
    # 0
    # 1
    print(num)
############################################
names_list = ['MOSTAFA', "AHMED", 'AMEER', 'KHALED']
#names_list[0] = names_list[0].lower()
for i in range(len(names_list)):
    # 1st loop i = 0, 2nd loop i = 1, i = 2, i = 3
    names_list[i] = names_list[i].lower()
print("My list in lower case", names_list)

my_name = 'KHALED'
new_name = my_name.lower()
print(my_name) # None
''.lower()
############################################
profile = {
    'id': 1,
    'name': 'ahmeD',
    'address': 'Moattam'
}

profile_list_of_tuples = profile.items() # [('id', 1), ('name', 'Ahmed'), ('address', 'Moattam'),]

for key, value in profile.items(): # 'item -> ('id', 1)
    # if the key is equal 'name' please make the value a title
    # 1st loop key: id, value:1
    # 2nd loop: key: name, value: ahmeD
    if key == 'name':
        profile[key] = value.title() # update

print(profile)

######################################################

''
"my name is mostafa. I am an instructor"
my_string = """
my name is mostafa
I am an instructor
"""
print(my_string)