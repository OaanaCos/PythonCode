### Whitespace & executions flow

print("Checking the weather for you!")


def weather_check():
    print("Looks great outside! Enjoy your trip.")


print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()
print("##########################")


### Parameters & arguments

# parameter = is the name defined in the parenthesis of the function and can be used in the function body
# argument = is the data that is passed in when we call the function and assigned to the parameter name

def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


generate_trip_instructions("Grand Central Station")


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print(car_rental_total + hotel_total + plane_ticket_price)


calculate_expenses(200, 100, 100, 5)
print("##########################")


### Types of arguments

# Positional arguments: arguments that can be called by their position in the function definition.
# When we call our function, the position of the arguments will be mapped to the positions defined
# in the function declaration.

# Keyword arguments: arguments that can be called by their name.
# We can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call.

# Default arguments: arguments that are given default values.
# We can provide a default value to an argument by using the assignment operator (=).
# This will happen in the function declaration rather than the function call.

def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print(
        "First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)


trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")
print("##########################")

### Built-in functions vs user defined functions

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
# The max() built-in function takes in a series of consecutive arguments and returns the max value.

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
# The min() built-in function takes in a series of consecutive arguments and returns the min value.

rounded_price = round(tshirt_price, 1)
print(rounded_price)
# The round() built-in function takes in two arguments. The first argument is the number we want to round,
# followed by an argument on how many decimal places we want to round it.
print("##########################")


### Variable Access

def print_count_locations():
    favorite_locations = "Paris, Norway, Iceland"
    print("There are 3 locations")


def show_favorite_locations():
    favorite_locations = "Paris, Norway, Iceland"
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations()

# If a variable lives outside of any function it can be accessed anywhere in the file.
print("##########################")

### Returns

# returned function value -> when there is a result from a function that is stored in a variable

current_budget = 3500.75


def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))


print_remaining_budget(current_budget)


def deduct_expense(budget, expense):
    return budget - expense


shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
print("##########################")


### Multiple returns

# return several values by separating them with a comma

def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)
print("##########################")


### Review

def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 " + name)


def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")


def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


trip_planner_welcome("Oana")
estimate = estimated_time_rounded(2.43)
destination_setup("Greece", "Amsterdam", estimate, "Car")
print("##########################")


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "colby"))
# should print True
print(same_name("Tina", "Ambe"))
# should print False


def append_sum(lst):
    for element in range(3):
        lst.append(lst[-2] + lst[-1])
    return lst

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))