# Filename: PersonaArcanaRandomizer.py
# Date: 7/5/26
# Author: Aoi | shadowsnowwolf

# Display output for a randomized Arcana based on the number of Arcanas the user wants
# Utlize a for loop to do it. Let user input decide the index for the loop iteration

import random


persona_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant","Lovers","Chariot","Justice","Hermit",
                   "Fortune","Strength","Hanged Man", "Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","Faith","Councillor")


def get_number_of_arcanas():
    number_of_arcanas = int(input("Please enter the number of Persona Arcanas to randomize: "))
    return number_of_arcanas

def randomize_arcana(number_index=0):
    number_of_arcanas = get_number_of_arcanas()
    randomized_arcanas = random.sample(persona_arcanas, number_of_arcanas)
    print("Randomized Persona Arcanas:")
    print("----------------------------")
    for arcana_index in range(number_of_arcanas):
            number_index += 1
            print(f"{number_index}. {randomized_arcanas[arcana_index]}")

while True:
    randomize_arcana()
    remprompt = input("\nWould you like to try again? (Enter y for yes, anything else to quit): ")
    if remprompt != "y":
        print("You exited the program.")
        break
