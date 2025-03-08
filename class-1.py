"Mostafa" # string
'Mostafa' # string
# 11 # integer
# 1.5 # float
# True # boolean
# False # boolean
username  = 'Mostafa'
username2 = 'Khaled'
username3 = True
# username = 1
print(type(username))
#############################
first_name = 'Mostafa' #snake case
last_name = 'Khaled'
full_name = first_name + ' ' + last_name
print(full_name)
print(type(''))
# print('Mostafa' + str(1))
######
print(int(1.5))
print(float(1))
print(1 + 1.5)
print("ha" * 5)
print(float("2.5"))
# "2.5" + 0.6
# 2.5 + 0.6
first_name = 'Mostafa'
 # camel case
####################
print(3 % 2) # remainder
#####################
name = "Khaled"
print(len(name)) # length
print(name[-1]) # last char in the string
print("Khaled Ahmed".index('a', )) # finding the position of char
print("Boy".count('B', 1, -1))
print("Ahmed".lower())
print("ahmed".upper())
print("mostafa mahmoud".title())
print("i am an engineer".capitalize())
print(" Mostafa Mahmoud".strip())
print(" Khaled Mohamed".lstrip())
print("Khaled Mohamed ".rstrip())
username = "Mostafa Mahmoud "
print(username.lower().rstrip())
#########################################
print("Hello World".replace("W", "w"))
print("Mostafa".islower())
print("HESHAM".isupper())
print("123".isdigit())
print("aly2".isalpha())
print("radar"[:4])
print("radar"[::-1]) # start:end(not incl.): step
username = "Ahmed"
# strings are immutable
name = 'ahmed'
# name[0] = 't'
print(name)
#################
print(f"My name is {username}")
print("My name is {}".format(username))
age = 30
print(f"I am {age} years old")
############
pi = 3.14159
print(f"The number is \n {pi:.2f}")
########################
x = 2
print(x >= 2)
#########################
my_list = [1, 'apple', 3, 4, True, 7]
print(len(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list[1])
print(my_list[-2])
print(my_list[::-1])
my_list[2] = 5 # update
print(my_list)
print(my_list.append(16)) # takes one item
print(my_list.append([8, 6])) # as one object (list)
print(my_list.insert(0, 9))
print(my_list)
print(my_list.extend([11, 12]))
print(my_list)
print(my_list[-3])
print(my_list[-3][-1]) # [8, 6]