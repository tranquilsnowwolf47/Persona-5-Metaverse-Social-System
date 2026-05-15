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

display_persona_skill_types()        
for i in range(loop_index):
    skill_type_choice = int(input(f"Enter skill category {skill_index} (1-17): "))
    skill_index += 1
    if skill_type_choice == 1:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light skills
                        print("\nLight Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill_index, skill in enumerate(PhysSkills.light_skills,start=1):
                            print(f"{skill_index}.", end=" ")
                            skill.display_simplified_info()
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.light_skills))
                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill_index, skill in enumerate(PhysSkills.medium_skills,start=1):
                            print(f"{skill_index}.", end=" ")
                            skill.display_simplified_info()
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.light_skills))    
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill_index, skill in enumerate(PhysSkills.heavy_skills,start=1):
                            print(f"{skill_index}.", end=" ")
                            skill.display_simplified_info()
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.light_skills))    
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill_index, skill in enumerate(PhysSkills.severe_skills,start=1):
                            print(f"{skill_index}.", end=" ")
                            skill.display_simplified_info()
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PhysSkills.light_skills))    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills       
                    print("\nPhys Skills: ")       
                    print("-----------------------------------------------------")  
                    skill_index = 1     
                    for group in PhysSkills.full_phys_skill_list:
                        for skill in group:
                            print(f"{skill_index}.", end=" ")
                            skill.display_simplified_info()
                            skill_index += 1 
                    # Stores the randomized skill object into the list 
                    randomized_skills.append(random.choice(PhysSkills.light_skills))        
                

def display_randomized_skills():     
    randomized_skill_index = 1       
    print("\nRandomized Skill List:")
    print("-----------------------------------------------------")  
    for skill in randomized_skills:
        print(f"{randomized_skill_index}. ",end=" ")
        skill.display_simplified_info()
        randomized_skill_index += 1
    
display_randomized_skills()

