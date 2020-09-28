food_list = []

food = str(input())

while food != "stop":
    food_list.append(food)
    food = input()

delete_food = "olives"

for f in food_list:
    if f == delete_food:
        food_list.remove(f)

for i in food_list:
    print(i)