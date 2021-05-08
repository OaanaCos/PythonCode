### Introduction to lists

heights = [61, 70, 67, 64, 65]
broken_heights = [65, 71, 59, 62]
print("##########################")

### What can a list contain?

ints_and_strings = [1, 2, 3, "four", "five", "six"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]
print("##########################")

### Empty list

my_empty_list = []
print("##########################")

### List methods

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)
print("##########################")

### Growing a list

orders = ["daisies", "periwinkle"]

print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)
print("##########################")

### Growing a list: plus +

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders

print(orders_combined)

broken_prices = [5, 3, 4, 5, 4] + [4]

print(broken_prices)
print("##########################")

### Accessing list elements

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]

print(employees[6])
print("##########################")

### Accessing list elements: negative index

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]

print(index5_element, last_element)
print("##########################")

### Modifying list elements

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"

print(garden_waitlist)

garden_waitlist[-1] = "Alex"

print(garden_waitlist)
print("##########################")

### Shrinking a list: remove

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

print(order_list)

order_list.remove("Flatbread")

print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list)
# The.remove() method will work on duplicate values in a list. .remove() will delete the first instance of a match
# for the provided element you want to delete.
print("##########################")

### Two-Dimensional (2D) lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

ages = [["Aaron", 15], ["Dhruti", 16]]
print(heights)
print(ages)
print("##########################")

### Accessing 2D lists

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][1]
print(ellies_score)
print("##########################")

### Modifying 2D lists

incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]

print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)
print("##########################")

### Review

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False

customer_data[1].remove(False)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
print("##########################")

### Mini Project: Gradebook

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[5][1] = 98

gradebook[2].remove(85)

gradebook[2].append("Pass")

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
print("##########################")

### Adding by index: insert

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0, "Pineapple")
print(front_display_list)
print("##########################")

### Removing by index: pop

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)
print("##########################")

### Consecutive lists: range

#The function range() takes a single input, and generates numbers starting at 0 and ending at the
# number before the input. So, if we want the numbers from 0 through 9, we use range(10) because
# 10 is 1 greater than 9.

number_list = range(10)
print(number_list)

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

range_five_three = range(5, 15, 3)
print(list(range_five_three))

range_diff_five = range(0, 40, 5)
print(list(range_diff_five))
print("##########################")

### Length

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list = range(2, 3000, 100)

long_list_len = len(long_list)
print(long_list_len)

range_list_length = len(range_list)
print(range_list_length)

# Range objects do not need to be converted to lists in order to determine their length.
print("##########################")

### Slicing I

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

print(beginning)

middle = suitcase[2:4]
print(middle)

### Slicing II

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)
print("##########################")

### Counting in a list

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)

### Sorting lists I

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]

names.sort()
print(names)

# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]

sorted_cities = cities.sort()
print(sorted_cities)

# The .sort() method does not return any value and thus does not need to be assigned to a variable.
# This is why we will see the value of None as our output for sorted_cities.

cities.sort(reverse=True)
print(cities)
print("##########################")

### Sorting lists II

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)

print(games)
print(games_sorted)

# The sorted() function is different from the .sort() method in two ways:
# 1. It comes before a list, instead of after as all built-in functions do.
# 2. It generates a new list rather than modifying the one that already exists.

# In contrast to the method .sort(), the built-in function sorted() will not modify the original list.
print("##########################")

### Review

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[:3]
print(first_3)

twin_beds = inventory.count("twin bed")
print(twin_beds)

removed_item = inventory.pop(4)
print(removed_item)

inventory.insert(10, "19th Century Bed Frame")
print(inventory)

inventory.sort()
sorted_inventory = sorted(inventory)
print(inventory)
print(sorted_inventory)

friends = ["Annabelle", "Greg", "Katya", "Sol"]
friends.insert(-2, "Gus")
print(friends)

###

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

message = "We sell " + str(num_pizzas) + " different kinds of pizza!"
print(message)

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

pizza_and_prices.pop(-1)
print(pizza_and_prices)

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

print("##########################")

### Zip

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

names_and_dogs_names = list(zip(owners, dogs_names))
print(names_and_dogs_names)
print("##########################")

