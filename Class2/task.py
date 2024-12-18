foods = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
calories = ("52", "96", "62", "605", "33", "68", "50", "33")

print (foods)
print (calories)

foods_list=list(foods)
calories_list=list(calories)
print(foods_list)
print(calories_list)


print(f"{foods[4]} and {calories[4]}")

print(f"{foods[-2]} and {calories[-2]}")

print(set(foods_list))

dict_foods = {"apple": 52, "banana": 96, "orange": 62, "mango": 605, "strawberry": 33, "grape": 68, "mandarin": 50, "strawberry": 33}
print(dict_foods)

dict_foods["tomato"] = 60
print(dict_foods)

dict_foods["grape"] = 50
print(dict_foods)

