




def roll_call_dwarves(names):
    count  = 1
    for i in names:
        print(f"{count}. {i}")
        count +=1
roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])


planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
def summon_captain_planet(planeteer_calls ):
    return[call.capitalize() + "!" for call in planeteer_calls]
summon_captain_planet(planeteer_calls)


short_words = ["puff", "go", "two"]
assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(words_list):
    return any(len(word) > 4 for word in words_list)
    
short_result = long_planeteer_calls(short_words)
assorted_result = long_planeteer_calls(assorted_words)

print(short_result)    # False
print(assorted_result) # True

######################################
######################################
def find_the_cheese(foods):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheese_types:
            return food
    return None

snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks)) #=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
print(find_the_cheese(soup)) #=> "cheddar"

ingredients = ["garlic", "rosemary", "bread"]
print(find_the_cheese(ingredients)) #=> None



