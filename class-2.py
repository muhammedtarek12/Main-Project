# reading data from a list
my_list = [1, 'apple', True, 1.5, 5]
print(my_list[2])
# add to the list
my_list.append(2)
print(my_list)
# add in a specified index(poisition)
my_list.insert(1, 'orange')
print(my_list)
# concatenate two lists using extend
my_list.extend([8, 9])
print(my_list)
# append a list as one object in a list, ex: [1, 2, 3, [4, 5]]
my_list.append([11, 12])
print("old list: ", my_list)
print(my_list[-1][0])
###############
# slicing then reversing
my_new_list = my_list[0:4][::-1]
print(my_new_list)
# [1, 2, 3][::-1]
# 1st type of concatenation
my_list = my_new_list + my_list[4:]
# 2nd type of concatenation
my_new_list.extend(my_list[4:])
print("My new list: ", my_new_list)
############################
# update
my_new_list[0] = False
print(my_new_list)
#################
fruits = ['apple', 'orange', 'watermelon', 'cherry']

my_cherry = fruits.remove('cherry')
print(my_cherry)

my_fruit = fruits.pop(1)
print(fruits)
print(my_fruit)
##################
fruits.clear()
print(fruits)
##########################################
my_tuple = (1, 1, 1.5, 'apple', True, [2, 3])
print("my tuple: ", my_tuple)
### read
print(my_tuple[-2])
## add
my_new_tuple = my_tuple + (6, 7)
print("my new tuple: ", my_new_tuple)
# how to get the tuple type
print(type(my_new_tuple))
# len of tuple
# print(len(my_tuple))
my_one_item_tuple = ('6',)
print(type(my_one_item_tuple))
print(my_tuple.count(1))
print(my_new_tuple.index(7))
print(len(my_new_tuple))
############################################## 3rd type of iterables
my_set = {1, 2.5, False, 'apple', (6, 7), 0, 9.5, True}
print(my_set)
# add
my_set.add('yellow')
print("My set:", my_set)
my_set.remove(9.5)
# my_set.clear()
print(my_set)
my_new_set = set()
#####
my_new_set = {}
######
my_set.discard(8)
print(my_set)
#########
my_set.copy()
###########
print(my_set.issuperset({'apple', 1}))
print({'apple', 1}.issubset(my_set))
print(my_set.isdisjoint({5, 2.5}))
############################
my_set.update({'yellow', 'green'})
print(my_set)
#########################
my_union_set = my_set.union({19, 20})
print("My union set: ", my_union_set)
################################
even_numbers_list = ['22', '2', '4', '66', '22', '6', '8',]
## intialize set
my_set = {3}
print(type(my_set))
my_set_2 = set()
print(type(my_set_2))
######
even_numbers = list(set(even_numbers_list))
print("My even numbers:", even_numbers)
############################################ dictionary
colors = ['red', 'green', 'blue', 'white']
colors_dict = {0: 'red', # key: value
               1: 'green',
               2: 'blue',
               3: 'white',
               4: 'yellow',
               5: 'orange',
               6: 'black'
               }
#read from a dict
print(colors_dict[0]) # keyolors_dict
# add
colors_dict[7] = 'brown'
print("My dictionary", colors_dict)

colors_dict[7] = 'dark blue'
print(colors_dict)

colors_dict.pop(7)
print(colors_dict)

new_dict = {'id': 1,
            'name': 'Ahmed',
            'mobile': '+201117270933',
            'gender': 'male',
            'children': ['Omar', 'Mostafa', 'Amr'],
            'is_employed': True,
            'addresses': [{'city': 'Cairo',
                          'postal_code': 11885,
                          'building': 'A01',
                          'street': 'Mohandseen'},
                         {'city': 'Alexandria',
                          'postal_code': 11855,
                          'building': 'A01',
                          'street': 'sedi beshr'}]
            }
print(new_dict['gender'])
print(new_dict['children'][-1])
# solution
print(new_dict['addresses'][-1]["street"])
###
new_dict['addresses'][-1]['postal_code'] = str(new_dict['addresses'][-1]['postal_code'])
print(type(new_dict['addresses'][-1]['postal_code']))
#####
# print(new_dict['salaries'])
print(new_dict.get('is_employed', False))
abdo_salary = new_dict.get('salary', 50000.00) # 2nd place is the default
#################
print("***************", new_dict)
new_dict.setdefault('salary', 50000.00) # this will apply if 'salary' key is not present
print("^^^^^^^^^^^^^^^", new_dict)
#################
print(list(new_dict.keys()))
print(list(new_dict.values()))
########
print("$$$$$$$$$$$$$$$$$$$$$$$$", new_dict.items()) # convert dict to [tuple, tuple]
dict_items = new_dict.items()
my_dict = dict(dict_items)
print("@@@@@@@@@@@@", my_dict)
