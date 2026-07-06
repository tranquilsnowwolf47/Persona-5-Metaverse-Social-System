# Filename: PersonaArcanaRandomizer.py
# Date: 7/5/26
# Author: Aoi | shadowsnowwolf

# Display output for a randomized Arcana based on the number of Arcanas the user wants
# Utlize a for loop to do it. Let user input decide the index for the loop iteration

import random


persona_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant","Lovers","Chariot","Justice","Hermit",
                   "Fortune","Strength","Hanged Man", "Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","Faith","Councillor")


arcana_index = int(input("Please enter the number of Persona Arcanas to randomize: "))
persona_index = 0

for i in range(arcana_index):
    for arcana in persona_arcanas:
        persona_index += 1
        print(f"{persona_index}. {random.choice(arcana)}")
