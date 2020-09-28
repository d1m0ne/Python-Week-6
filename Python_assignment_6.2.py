food_list = []

food = str(input())

while food != "stop":
    food_list.append(food)
    food = input()

print ("Please select a food to delete from the list.")

delete_food = str(input())

for f in food_list:
    if f == delete_food:
        food_list.remove(f)

for i in food_list:
    print(i)