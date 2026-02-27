count = 0

while True:  # This condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # Exit loop if count >= 5

n = 0
zoo = ["lion", "tiger", "elephant", "giraffe", "python"]
while True:                         # This condition cannot possibly be false
    animal = zoo.pop()       # Extract one element from the end of the list
    print(animal)
    n += 1
    # Add the condition to exit the loop
    if n == 3:
        break
        # Exit the loop

print(zoo)
