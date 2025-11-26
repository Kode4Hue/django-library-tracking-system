import random
# rand_list = 
n = 10
rand_list = random.sample(range(1, 20), n)
print(rand_list)

# list_comprehension_below_10 =
list_comprehension_below_10 = [x for x in rand_list if x < 10]
print("filter list below 10 using list comprehension")
print(list(list_comprehension_below_10))

# list_comprehension_below_10 = 
list_comprehension_below_10 = [] # empty the list comprehension to ensure it is empty
print("filter list below 10 using filter")
# print(list_comprehension_below_10)
list_comprehension_below_10 =  filter(lambda x: x < 10, rand_list)
print(list(list_comprehension_below_10))