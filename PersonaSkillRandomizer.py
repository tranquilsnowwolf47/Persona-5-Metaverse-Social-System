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


# Bugs: 
# Severe skills where there aren't any yet
# elec skill medium (none yet)
# bless skill heavy (none yet)

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
            # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Fire skill was added.\n")
                        randomized_skills.append(random.choice(FireSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Fire skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(FireSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Fire skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(FireSkills.heavy_skills))    
                    # Dev note: There's no Severe Fire skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Fire skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(FireSkills.severe_skills)) 
                        if random.choice(FireSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_fire_skills = FireSkills.light_skills + FireSkills.medium_skills + FireSkills.heavy_skills + FireSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Fire skill was added.\n")
                    randomized_skills.append(random.choice(all_fire_skills)) 

    # Ice Randomizer
    elif skill_type_choice == 4:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Ice skill was added.\n")
                        randomized_skills.append(random.choice(IceSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Ice skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(IceSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Ice skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(IceSkills.heavy_skills))    
                    # Dev note: There's no Severe Ice skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Ice skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(IceSkills.severe_skills)) 
                        if random.choice(IceSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_ice_skills = IceSkills.light_skills + IceSkills.medium_skills + IceSkills.heavy_skills + IceSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Gun skill was added.\n")
                    randomized_skills.append(random.choice(all_ice_skills)) 

    # Elec Randomizer
    elif skill_type_choice == 5:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Elec skill was added.\n")
                        randomized_skills.append(random.choice(ElecSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Elec skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(ElecSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Elec skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(ElecSkills.heavy_skills))    
                    # Dev note: There's no Severe Elec skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Elec skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(ElecSkills.severe_skills)) 
                        if random.choice(ElecSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_elec_skills = ElecSkills.light_skills + ElecSkills.medium_skills + ElecSkills.heavy_skills + ElecSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Gun skill was added.\n")
                    randomized_skills.append(random.choice(all_elec_skills)) 

    # Wind Randomizer
    elif skill_type_choice == 6:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Wind skill was added.\n")
                        randomized_skills.append(random.choice(WindSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Wind skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(WindSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Wind skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(WindSkills.heavy_skills))    
                    # Dev note: There's no Severe Wind skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Wind skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(WindSkills.severe_skills)) 
                        if random.choice(WindSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_wind_skills = WindSkills.light_skills + WindSkills.medium_skills + WindSkills.heavy_skills + WindSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Gun skill was added.\n")
                    randomized_skills.append(random.choice(all_wind_skills)) 

    # Psy Randomizer
    elif skill_type_choice == 7:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Psy skill was added.\n")
                        randomized_skills.append(random.choice(PsySkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Psy skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PsySkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Psy skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PsySkills.heavy_skills))    
                    # Dev note: There's no Severe Psy skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Psy skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(PsySkills.severe_skills)) 
                        if random.choice(PsySkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_psy_skills = PsySkills.light_skills + PsySkills.medium_skills + PsySkills.heavy_skills + PsySkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Gun skill was added.\n")
                    randomized_skills.append(random.choice(all_psy_skills)) 

    # Nuke Randomizer
    elif skill_type_choice == 8:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Nuke skill was added.\n")
                        randomized_skills.append(random.choice(NukeSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Nuke skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(NukeSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Nuke skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(NukeSkills.heavy_skills))    
                    # Dev note: There's no Severe Nuke skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Nuke skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(NukeSkills.severe_skills)) 
                        if random.choice(NukeSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_nuke_skills = NukeSkills.light_skills + NukeSkills.medium_skills + NukeSkills.heavy_skills + NukeSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Nuke skill was added.\n")
                    randomized_skills.append(random.choice(all_nuke_skills)) 

    # Bless Randomizer
    elif skill_type_choice == 9:
        # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Bless skill was added.\n")
                        randomized_skills.append(random.choice(BlessSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Bless skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(BlessSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Bless skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(BlessSkills.heavy_skills))    
                    # Dev note: There's no Severe Bless skills yet
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Bless skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(BlessSkills.severe_skills)) 
                        if random.choice(BlessSkills.severe_skills) == None:
                                randomized_skills.append("")    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_bless_skills = BlessSkills.light_skills + BlessSkills.medium_skills + BlessSkills.heavy_skills + BlessSkills.severe_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Bless skill was added.\n")
                    randomized_skills.append(random.choice(all_bless_skills)) 

    # Curse Randomizer
    elif skill_type_choice == 10:
            # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("\nDamage grades:")
                    for index, damage_grade in enumerate(damage_grades,start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Stores the randomized skill object into the list 
                        print("\nRandom Light Curse skill was added.\n")
                        randomized_skills.append(random.choice(CurseSkills.light_skills))
                    elif damage_grade_choice == 2:
                        print("\nRandom Medium Curse skill was added.")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(CurseSkills.medium_skills))    
                    elif damage_grade_choice == 3:
                        print("\nRandom Heavy Curse skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(CurseSkills.heavy_skills))    
                    elif damage_grade_choice == 4:
                        print("\nRandom Severe Curse skill was added.\n")
                        # Stores the randomized skill object into the list 
                        randomized_skills.append(random.choice(CurseSkills.severe_skills)) 
                    # Randomize Instant Kill skill
                    elif damage_grade_choice == 5:
                         print("\nRandom Instant Kill Curse skill was added.\n")
                         # Stores the randomized skill object into the list
                         randomized_skills.append(random.choice(CurseSkills.instant_kill_skills))
                    
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    all_curse_skills = CurseSkills.light_skills + CurseSkills.medium_skills + CurseSkills.heavy_skills + CurseSkills.severe_skills + CurseSkills.instant_kill_skills
                    # Stores the randomized skill object into the list 
                    print("\nRandom Curse skill was added.\n")
                    randomized_skills.append(random.choice(all_curse_skills)) 

    # Buff Randomizer
    elif skill_type_choice == 11:
        print("Would you like to randomize a Singular Buff skill, AOE Buff skill, or both?")
        buff_format_choice = int(input("Enter a choice (1-3): "))
        # Stores a randomized singular buff skill
        if buff_format_choice == 1:
            print("\nRandom Singular Buff skill was added.\n")
            randomized_skills.append(random.choice(BuffSkills.singular_skills))
        # Stores a randomized AOE buff skill
        elif buff_format_choice == 2:
            print("\nRandom AOE Buff skill was added.\n")
            randomized_skills.append(random.choice(BuffSkills.AOE_skills))
        # Stores a randomized buff skill
        elif buff_format_choice == 3:
           all_buff_skills = BuffSkills.singular_skills + BuffSkills.AOE_skills
           print("\nRandom Buff skill was added.\n")
           randomized_skills.append(random.choice(all_buff_skills))
    
    # Debuff Randomizer
    elif skill_type_choice == 12:
        print("Would you like to randomize a Singular Debuff skill, AOE Debuff skill, or both?")
        debuff_format_choice = int(input("Enter a choice (1-3): "))
        # Stpres a ramdomized singular debuff skill
        if debuff_format_choice == 1:
            print("\nRandom Debuff skill was added.\n")
            randomized_skills.append(random.choice(DebuffSkills.singular_skills))
        # Stores a ramdomized AOE debuff skill
        elif debuff_format_choice == 2:
            print("\nRandom Debuff skill was added.\n")
            randomized_skills.append(random.choice(DebuffSkills.AOE_skills))
        # Stores a randomized debuff skill
        elif debuff_format_choice == 3:
            all_debuff_skills = DebuffSkills.singular_skills + DebuffSkills.AOE_skills
            print("\nRandom Debuff skill was added.\n")
            randomized_skills.append(random.choice(all_debuff_skills))

    # Passive Buff Randomizer
    elif skill_type_choice == 13:
        print("\nRandom Passive Buff was added.\n")
        randomized_skills.append(random.choice(PassiveBuffSkills.passive_buffs))

    # HP Recovery Randomizer
    elif skill_type_choice == 14:
        print("Would you like to randomize a Light HP Recovery skill, Moderate HP Recovery skill, Full HP Recovery skills, or All HP Recovery skils?")
        hp_recovery_skill_format = int(input("Enter a choice (1-4): "))
        if hp_recovery_skill_format == 1:
            print("\nRandom Light HP Recovery skill added.\n")
            randomized_skills.append(random.choice(HPRecoverySkills.light_recovery_skills))
        elif hp_recovery_skill_format == 2:
            print("\nRandom Moderate HP Recovery skill added.\n")
            randomized_skills.append(random.choice(HPRecoverySkills.moderate_recovery_skills))
        elif hp_recovery_skill_format == 3:
            print("\nRandom Full HP Recovery skill added.\n")
            randomized_skills.append(random.choice(HPRecoverySkills.full_recovery_skills))
        elif hp_recovery_skill_format == 4:
            all_hp_recovery_skills = HPRecoverySkills.light_recovery_skills + HPRecoverySkills.moderate_recovery_skills + HPRecoverySkills.full_recovery_skills
            print("\nRandom HP Recovery skill added.\n")
            randomized_skills.append(random.choice(all_hp_recovery_skills))
             
    # Ailment Recovery Randomizer
    elif skill_type_choice == 15:
        print("\nAilment Recovery skills are not yet available, sorry :(")
        print("(Coming soon)")

    # Passives Randomizer
    elif skill_type_choice == 16:
        print("Would you like to randomize a Normal Passive skill, Affinity Passive skill or both?")
        passive_skill_format = int(input("Enter a choice (1-3): "))
        # Stores a randomized normal passive skill
        if passive_skill_format == 1:
            print("\nRandom Passive skill was added.\n")
            randomized_skills.append(random.choice(PassiveSkills.normal_passive_skills))
        # Stores a randomized affinity passive skill
        elif passive_skill_format == 2:
            print("\nRandom Passive skill was added.\n")
            randomized_skills.append(random.chocie(PassiveSkills.affinity_passive_skills))
        # Stores a randomized passive skill
        elif passive_skill_format == 3:
            all_passive_skills = PassiveSkills.normal_passive_skills + PassiveSkills.affinity_passive_skills
            print("\nRandom Passive skill was added.\n")
            randomized_skills.append(random.choice(all_passive_skills))

    # Status Ailment Randomizer
    elif skill_type_choice == 17:
        print("\nStatus Ailment skills are not yet available, sorry :(")
        print("(Coming soon)")

else:
    print("You did not enter a valid skill type.")



    
display_randomized_skills()

