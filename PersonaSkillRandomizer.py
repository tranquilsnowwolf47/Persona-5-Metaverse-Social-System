# Filename: PersonaSkillRandomizer.py
# Date: 5/15/26
# Author: Aoi | shadowsnowwolf
# Description: A program that randomizes from Persona skills based on the user's skill
# category choice. Significantly optimizes Persona building when the user doesn't know
# What skills to put on their Persona(s)

# Use a while loop and a for loop
# if the user doesnt like the skill, reroll with a while loop
# Use random.choice to cycle through skill options
# ask for an element, and a damage grade possibly
# if they don't care about the damage grade, just cycle through all skills of that element
# for the 8 skills that are to the user's liking, append them to a list or whatever


# I need the Persona's name
# Arcana


# Update needed:
# Later on, make it so that you can't have the same skill randomized

import random
import PhysSkills
import GunSkills
import FireSkills
import IceSkills
import ElecSkills
import WindSkills
import PsySkills
import NukeSkills
import BlessSkills
import CurseSkills
import BuffSkills
import DebuffSkills
import PassiveBuffSkills
import HPRecoverySkills
import AilmentRecoverySkills
import PassiveSkills


randomized_skills = ()

# A while loop will iterate 8 times, putting 8 skills in the tuple. 
# If the user doesn't like it, they can refresh.


# Randomize the skill and display the skill name

skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery", "Passives", "Status Ailment") # A tuple that will hold the list of all skill types 
skill_type_numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
damage_grades = ("Light", "Medium", "Heavy", "Severe", "Instant Kill")


loop_index = int(input("Enter the number of skills you'd like to randomize: "))
skill_index = 1
randomized_skills = []

def display_persona_skill_types():
    print("Persona Skill Types:")
    print("-----------------------------")
    for index, skill_type in enumerate(skill_types,start=1):
        print(f"{index}. {skill_type}")

def display_randomized_skills():     
    randomized_skill_index = 1       
    print("\nRandomized Skill List:")
    print("-----------------------------------------------------")  
    for skill in randomized_skills:
        print(f"{randomized_skill_index}.",end=" ")
        skill.display_simplified_info()
        randomized_skill_index += 1

#while True:
for i in range(loop_index):
    display_persona_skill_types()
    skill_type_choice = int(input(f"\nEnter skill category #{i + 1} (1-17): "))
    # Phys Randomizer
    if skill_type_choice == 1:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Phys skill was added.\n")
                        randomized_skills.append(random.choice(PhysSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Phys skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Phys skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.heavy_skills))    
                    # Dev note: There's no Severe Phys skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Phys skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.severe_skills)) 
                        if random.choice(PhysSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_phys_skills = PhysSkills.light_skills + PhysSkills.medium_skills + PhysSkills.heavy_skills + PhysSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Phys skill was added.\n")
                    randomized_skills.append(random.choice(all_phys_skills))  
                
    # Gun Randomizer
    elif skill_type_choice == 2:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Gun skill was added.\n")
                        randomized_skills.append(random.choice(GunSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Gun skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(GunSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Gun skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(GunSkills.heavy_skills))    
                    # Dev note: There's no Severe Gun skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Gun skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(GunSkills.severe_skills)) 
                        if random.choice(GunSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_gun_skills = GunSkills.light_skills + GunSkills.medium_skills + GunSkills.heavy_skills + GunSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Gun skill was added.\n")
                    randomized_skills.append(random.choice(all_gun_skills))  

    # Fire Randomizer
    elif skill_type_choice == 3:
        pass

    # Ice Randomizer
    elif skill_type_choice == 4:
        pass

    # Elec Randomizer
    elif skill_type_choice == 5:
        pass

    # Wind Randomizer
    elif skill_type_choice == 6:
        pass

    # Psy Randomizer
    elif skill_type_choice == 7:
        pass

    # Nuke Randomizer
    elif skill_type_choice == 8:
        pass

    # Bless Randomizer
    elif skill_type_choice == 9:
        pass

    # Curse Randomizer
    elif skill_type_choice == 10:
        pass

    # Buff Randomizer
    elif skill_type_choice == 11:
        pass

    # Debuff Randomizer
    elif skill_type_choice == 12:
        pass

    # Passive Buff Randomizer
    elif skill_type_choice == 13:
        pass

    # HP Recovery Randomizer
    elif skill_type_choice == 14:
        pass

    # Ailment Recovery Randomizer
    elif skill_type_choice == 15:
        pass

    # Passives Randomizer
    elif skill_type_choice == 16:
        pass

    # Status Ailment Randomizer
    elif skill_type_choice == 17:
        pass

else:
    print("You did not enter a valid skill type.")



    
display_randomized_skills()

