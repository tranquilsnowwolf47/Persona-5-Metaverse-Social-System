# Filename: PersonaSkillListProgramV1.py 
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf

# Processing:
# A program that has a full list of all Persona skills
# Imports the Skill lists as modules 

# Note to self:
# Throw some try-except block in that bad boy


# Imports the modules of all the skill categories 
import PhysSkills
import GunSkills
import FireSkills
import IceSkills
import ElecSkills
import WindSkills
import PsySkills
import NukeSkillList
import BlessSkills
import CurseSkills
import BuffSkills
import DebuffSkills
import PassiveBuffList
import HPRecoverySkillList
import AilmentRecoverySkillList
import PassiveSkillList

# A tuple that holds all Persona skill types that the user whill be able to choose from
skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives", "Status Ailment") 

# The indexes for the skill types which correlate to each skill type
skill_types_indexes = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

# Elemental skills that reference indexes from valid skill types 
elemental_skills = (skill_types[0],skill_types[1],skill_types[2],skill_types[3],
skill_types[4],skill_types[5], skill_types[6], skill_types[7], skill_types[8],
skill_types[9])

# Damage grade for elemental skills 
damage_grades = ("Light", "Medium", "Heavy", "Severe", "Instant Kill")
damage_grades_indexes = (1,2,3,4)
hp_recovery_grades = ("Light", "Moderate", "Full")


while True:
    # Display the skill types to the user 
    print("Persona Skill Types:")
    print("-----------------------------")
    for index, skill_type in enumerate(skill_types,start=1):
        print(f"{index}. {skill_type}")

    # Get the skill type from the user
    skill_type_choice = int(input("\nPlease enter a skill type (1-17): "))

    # If the skill type is in the index range, proceed with operations
    if skill_type_choice in skill_types_indexes:
            # Phys  | Debugged
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
                        for skill in PhysSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill in PhysSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill in PhysSkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Phys Skills:")
                        print("-----------------------------------------------------")    
                        for skill in PhysSkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills       
                    print("\nPhys Skills: ")       
                    print("-----------------------------------------------------")       
                    for group in PhysSkills.full_phys_skill_list:
                        for skill in group:
                            skill.display_simplified_info()
            # Gun | Debugged
            elif skill_type_choice == 2:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light skills
                        print("\nLight Gun Skills:")
                        print("-----------------------------------------------------")  
                        for skill in GunSkills.light_skills:
                            skill.display_simplified_info()     

                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Gun Skills:")
                        print("-----------------------------------------------------")    
                        for skill in GunSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Gun Skills:")
                        print("-----------------------------------------------------") 
                        for skill in GunSkills.heavy_skills:  
                            skill.display_simplified_info() 
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Gun Skills:")
                        print("-----------------------------------------------------") 
                        for skill in GunSkills.severe_skills:
                            skill.display_simplified_info()   

                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nGun Skills:")
                    print("-----------------------------------------------------")    
                    for group in GunSkills.full_gun_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Fire | Debugged
            elif skill_type_choice == 3:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light skills
                        print("\nLight Fire Skills:")
                        print("-----------------------------------------------------")    
                        for skill in FireSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Fire Skills:")
                        print("-----------------------------------------------------")    
                        for skill in FireSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Fire Skills:")
                        print("-----------------------------------------------------")    
                        for skill in FireSkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Fire Skills:")
                        print("-----------------------------------------------------")    
                        for skill in FireSkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nFire Skills:")
                    for group in FireSkills.full_fire_skill_list:
                        for skill in group:
                            skill.display_simplified_info()
                            
            # Ice | Debugged
            elif skill_type_choice == 4:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light skills
                        print("\nLight Ice Skills:")
                        print("-----------------------------------------------------")    
                        for skill in IceSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Ice Skills:")
                        print("-----------------------------------------------------")    
                        for skill in IceSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Ice Skills:")
                        print("-----------------------------------------------------")    
                        for skill in IceSkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Ice Skills:")
                        print("-----------------------------------------------------")    
                        for skill in IceSkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nIce Skills:")
                    print("-----------------------------------------------------")    
                    for group in IceSkills.full_ice_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Elec | Debugged
            elif skill_type_choice == 5:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light skills
                        print("\nLight Elec Skills:")
                        print("-----------------------------------------------------")    
                        for skill in ElecSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Elec Skills:")
                        print("-----------------------------------------------------")    
                        for skill in ElecSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Elec Skills:")
                        print("-----------------------------------------------------")    
                        for skill in ElecSkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Elec Skills:")
                        print("-----------------------------------------------------")    
                        for skill in ElecSkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nElec Skills:")
                    print("-----------------------------------------------------")    
                    for group in ElecSkills.full_elec_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Wind | Debugged
            elif skill_type_choice == 6:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light skills
                        print("\nLight Wind Skills:")
                        print("-----------------------------------------------------")    
                        for skill in WindSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium skills
                        print("\nMedium Wind Skills:")
                        print("-----------------------------------------------------")    
                        for skill in WindSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy skills
                        print("\nHeavy Wind Skills:")
                        print("-----------------------------------------------------")    
                        for skill in WindSkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Wind Skills:")
                        print("-----------------------------------------------------")    
                        for skill in WindSkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nWind Skills:")
                    print("-----------------------------------------------------")    
                    for group in WindSkills.full_wind_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Psy | Debugged
            elif skill_type_choice == 7:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light Psy skills
                        print("\nLight Psy Skills: ")
                        print("-----------------------------------------------------")    
                        for skill in PsySkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium Psy skills
                        print("\nMedium Psy Skills:")
                        print("-----------------------------------------------------")    
                        for skill in PsySkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy Psy skills
                        print("\nHeavy Psy Skills:")
                        print("-----------------------------------------------------")    
                        for skill in PsySkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe Psy skills
                        print("\nSevere Psy Skills:")
                        print("-----------------------------------------------------")    
                        for skill in PsySkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nPsy Skills:")
                    print("-----------------------------------------------------")    
                    for group in PsySkills.full_psy_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Nuke | Debugged
            elif skill_type_choice == 8:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light Nuke skills
                        print("\nLight Nuke Skills:")
                        print("-----------------------------------------------------")    
                        for skill in NukeSkillList.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium Nuke skills
                        print("\nMedium Nuke Skills:")
                        print("-----------------------------------------------------")    
                        for skill in NukeSkillList.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy Nuke skills
                        print("\nHeavy Nuke Skills:")
                        print("-----------------------------------------------------")    
                        for skill in NukeSkillList.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe Nuke skills
                        print("\nSevere Nuke Skills:")
                        print("-----------------------------------------------------")    
                        for skill in NukeSkillList.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nNuke Skills:")
                    print("-----------------------------------------------------")    
                    for group in NukeSkillList.full_nuke_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Bless | Debugged
            elif skill_type_choice == 9:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades[0:4],start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter a damage grade (1-4): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light Bless skills
                        print("\nLight Bless Skills:")
                        print("-----------------------------------------------------")    
                        for skill in BlessSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium Bless skills
                        print("\nMedium Bless Skills:")
                        print("-----------------------------------------------------")    
                        for skill in BlessSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy Bless skills
                        print("\nHeavy Bless Skills:")
                        print("-----------------------------------------------------")    
                        for skill in BlessSkills.heavy_skills:
                            skill.display_simplflified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe Bless skills
                        print("\nSevere Bless Skills:")
                        print("-----------------------------------------------------")    
                        for skill in BlessSkills.severe_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nBless Skills:")
                    print("-----------------------------------------------------")    
                    for group in BlessSkills.full_bless_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Curse | Debugged
            elif skill_type_choice == 10:
                # Ask the user if they'd like to see a specific damage grade for the skill type
                damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
                if damage_grade_validation == "Y":
                    print("Damage grades:")
                    for index, damage_grade in enumerate(damage_grades,start=1):
                        print(f"{index}. {damage_grade}")
                    damage_grade_choice = int(input("Enter an option choice (1-5): "))
                    if damage_grade_choice == 1:
                        # Display the list of Light Curse skills
                        print("\nLight Curse Skills:")
                        print("-----------------------------------------------------")    
                        for skill in CurseSkills.light_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 2:
                        # Display the list of Medium Curse skills
                        print("\nMedium Curse Skills:")
                        print("-----------------------------------------------------")    
                        for skill in CurseSkills.medium_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 3:
                        # Display the list of Heavy Curse skills
                        print("\nHeavy Curse Skills:")
                        print("-----------------------------------------------------")    
                        for skill in CurseSkills.heavy_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 4:
                        # Display the list of Severe skills
                        print("\nSevere Curse Skills:")
                        print("-----------------------------------------------------")    
                        for skill in CurseSkills.severe_skills:
                            skill.display_simplified_info()
                    elif damage_grade_choice == 5:
                        # Display the list of Curse Instant kill skills 
                        print("\nCurse Instant Kill Skills:")
                        print("-----------------------------------------------------")    
                        for skill in CurseSkills.instant_kill_skills:
                            skill.display_simplified_info()
                # If they don't want to see a specific damage grade, just display the list of all skills
                else:
                    # Display all skills 
                    print("\nCurse Skills:")
                    print("-----------------------------------------------------")    
                    for group in CurseSkills.full_curse_skill_list:
                        for skill in group:
                            skill.display_simplified_info()
        
            # if the user chooses other than an elemental skill
            # Buffs | Debugged
            # --------------------------------------------------------------
            elif skill_type_choice == 11: 
                valid_buff_format_choices = ("Singular", "AOE", "Both")
                buff_format_choice_indexes = (1,2,3)
                print("Buff choices:")
                for index, buff_choice in enumerate(valid_buff_format_choices,start=1):
                    print(f"{index}. {buff_choice}")
                print("Would you like to see Singular Buff skills, AOE Buff skills, or both?")
                buff_format_choice = int(input("Enter a choice (1-3): "))
                # Display the list of all singular buff skills
                if buff_format_choice == 1:
                    print("\nSingular Buff Skills:")
                    print("-----------------------------------------------------")    
                    for skill in BuffSkills.singular_skills:
                        skill.display_simplified_info()
                # Display the list of AOE buff skills 
                elif buff_format_choice == 2:
                    print("\nAOE Buff Skills:")
                    print("-----------------------------------------------------")    
                    for skill in BuffSkills.AOE_skills:
                        skill.display_simplified_info()
                # Display the list of all buffs skills
                elif buff_format_choice == 3:
                    print("\nBuff Skills:")
                    print("-----------------------------------------------------")    
                    for group in BuffSkills.full_buff_skill_list:
                        for buff in group:
                            buff.display_simplified_info()
                    
            # Debuffs 
            # --------------------------------------------------------------
            elif skill_type_choice == 12:
                valid_debuff_format_choices = ("Singular", "AOE", "Both")
                debuff_format_choice_indexes = (1,2,3)
                print("Debuff choices:")
                for index, debuff_choice in enumerate(valid_debuff_format_choices,start=1):
                    print(f"{index}. {debuff_choice}")
                print("Would you like to see Singular Debuff skills, AOE Debuff skills, or both?")
                debuff_format_choice = int(input("Enter a choice (1-3): "))
                # Display the list of all singular debuff skills
                if debuff_format_choice == 1:
                    print("\nSingular Debuff Skills:")
                    print("-----------------------------------------------------")    
                    for skill in DebuffSkills.singular_skills:
                        skill.display_simplified_info()

                # Display the list of all AOE debuff skills
                elif debuff_format_choice == 2:
                    print("\nAOE Debuff Skills:")
                    print("-----------------------------------------------------")    
                    for skill in DebuffSkills.aoe_skills:
                        skill.display_simplified_info()

                # Display the list of all debuff skills
                elif debuff_format_choice == 3:
                    print("\nDebuff Skills:")
                    print("-----------------------------------------------------")  
                    for group in DebuffSkills.full_debuff_skills:
                        for skill in group:
                            skill.display_simplified_info()
                
            # Passive Buffs   
            # --------------------------------------------------------------
            elif skill_type_choice == 13:
                print("\nPassive Buff Skills:")
                for skill in PassiveBuffList.passive_buffs:
                    skill.display_simplified_info()

            # HP Recovery
            # --------------------------------------------------------------
            elif skill_type_choice == 14:
                pass

            # Ailment Recovery
            elif skill_type_choice == 15:
                print("Ailment Recovery skills are not yet available, sorry :(")
                print("(Comning soon)")

            # Passives
            # --------------------------------------------------------------
            elif skill_type_choice == 16:
                valid_passive_choices = ("Normal", "Affinity", "Both")
                passive_format_choice_indexes = (1,2,3)
                print("Passive choices:")
                for index, passive_choice in enumerate(valid_passive_choices,start=1):
                    print(f"{index}. {passive_choice}")
                print("Would you like to see Normal passive skills, affinity passive skills or both?")
                passive_format_choice = int(input("Enter a chioce (1-3): "))
                # Display the list of normal passives
                if passive_format_choice == 1:
                    for skill in PassiveSkillList.normal_passive_skills:
                        skill.display_simplified_info()
                # Display the list of affinity passives
                elif passive_format_choice == 2:
                    for skill in PassiveSkillList.affinity_passive_skills:
                        skill.display_simplified_info()
                # Display all passive skills
                elif passive_format_choice == 3:
                    print("Passive Skills:")
                    for group in PassiveSkillList.full_passive_skill_list:
                        for skill in group:
                            skill.display_simplified_info()

            # Status Ailment
            # --------------------------------------------------------------
            elif skill_type_choice == 17:
                print("Status Ailment skills are not yet available, sorry :(")
                print("(Comning soon)")

    # If the user didn't enter a valid skill type, let them know
    else:
        print("You did not enter a valid skill type.")

    loop_input = input("\nWould you like to try again? (Enter 'y' for yes, anything else to exit): ").lower()
    if loop_input != "y":
        print("Exited the program.")
        break

            


    
