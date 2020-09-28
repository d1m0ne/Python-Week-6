food_list = []

food = input()

while food != "stop":
    food_list.append(food)
    food = input()

for i in food_list:
    print(i)