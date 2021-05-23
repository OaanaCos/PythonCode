### For loops: introduction

# for loops -> a type of definite iteration
# we will know in advance how many times the loop will need to iterate because we will be working on
# a collection with a predefined length.

# with for loops, on each iteration, we will be able to perform an action on each element of the collection.

### 1. A for keyword indicates the start of a for loop.
### 2. A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
### 3. An in keyword separates the temporary variable from the collection used for iteration.
### 4. A <collection> to loop over. In our examples, we will be using a list.
### 5. An <action> to do anything on each iteration of the loop.

### Temporary Variables: a temporary variable’s name is arbitrary and does not need to be defined beforehand.

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)
print("##########################")

### For loops: using range

promise = "I will finish the python loops module!"

for word in range(5):
    print(promise)
print("##########################")

### While loops: introduction

# while loops -> a type of indefinite iteration

# A while loop performs a set of instructions as long as a given condition is true.

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")
print("##########################")

### While loops: lists

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1
print("##########################")

### Infinite loops

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(students_period_B)
print("##########################")

### Loop control: break

# break loop control statement -> stop iteration from inside the loop

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break
print("##########################")

### Loop control: continue

# the continue control statement is usually paired with some form of a conditional (if/elif/else)

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 21:
        continue
    print(age)
print("##########################")

### Nested loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for scoops in location:
        scoops_sold += scoops
print(scoops_sold)
print("##########################")

### List comprehensions: introduction

# new_list = [<expression> for <element> in <collection>]

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]

print(scaled_grades)
print("##########################")

# List comprehensions: conditionals

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
    if num < 0:
        only_negative_doubled.append(num * 2)

print(only_negative_doubled)

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers]
print(doubled)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)
print("##########################")

### Review

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Another option:
single_digits_1 = list(range(10))

squares = []

for digit in single_digits:
    squares.append(digit ** 2)
    print(digit)
print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)
print("##########################")

###

numbers = [1, 1, 2, 3]
for number in numbers:
    if number % 2 == 0:
        break
    print(number)
