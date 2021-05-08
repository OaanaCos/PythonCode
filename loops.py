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




