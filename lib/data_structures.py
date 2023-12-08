spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
        new_list=  [food["name"] for food in spicy_foods]
        return new_list
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
     spiciest_foods = [food for food in spicy_foods if food["heat_level"]>5]
     return spiciest_foods
print (get_spiciest_foods(spicy_foods))
                       

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
          print( food["name"] + " " + "("+ (food["cuisine"])+ ")" + " | " + "Heat Level: "+ "🌶"*(food["heat_level"]))
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     filtered_foods= [food for food in spicy_foods if food["cuisine"]== cuisine]
     for food in filtered_foods:
        return food
print (get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
     filter_food= [food for food in spicy_foods if food["heat_level"]>5]
     for food in filter_food:
          print(food["name"] +" "+ "("+ food["cuisine"] + ")" + " | "+ "Heat Level:"+ "🌶"* food["heat_level"] )
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level
average_heat_level = get_average_heat_level(spicy_foods)
print(average_heat_level)

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)
print(spicy_foods)