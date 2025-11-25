# For EXP rates 



EXP_PER_ACTION = 3

# EXP rates for ambushed encounters
RED_SHADOW_AMBUSHED = 8 * EXP_PER_ACTION
YELLOW_SHADOW_AMBUSHED = 7 * EXP_PER_ACTION
BLUE_SHADOW_AMBUSHED = 6 * EXP_PER_ACTION
ambushed_EXP = [RED_SHADOW_AMBUSHED,
            YELLOW_SHADOW_AMBUSHED,
            BLUE_SHADOW_AMBUSHED]

valid_ambushed_inputs = ["RSA","YSA","BSA"]


# EXP rates for normal encounters 
red_shadow_normal = 7 * EXP_PER_ACTION
yellow_shadow_normal = 6 * EXP_PER_ACTION
blue_shadow_normal = 5 * EXP_PER_ACTION

normal_EXP = [red_shadow_normal, 
          yellow_shadow_normal, 
          blue_shadow_normal]

valid_normal_inputs = ["RSN","YSN","BSN"]


# EXP rates for ambushing encounters 
red_shadow_ambushing = 5 * EXP_PER_ACTION
yellow_shadow_ambushing = 4 * EXP_PER_ACTION
blue_shadow_ambushing = 3 * EXP_PER_ACTION
ambushing_EXP = [red_shadow_ambushing,
             yellow_shadow_ambushing,
             blue_shadow_ambushing]

valid_ambushing_inputs = ["RSAI","YSAI","BSAI"]


# EXP rates for skill encounters 
heavy_skill = 8 * EXP_PER_ACTION
medium_skill = 7 * EXP_PER_ACTION
light_skill = 6 * EXP_PER_ACTION
skill_EXP = [heavy_skill, medium_skill, light_skill]

valid_skill_inputs = ["HS","MS","LS"]

loop_index = 4

# accumulator variable 
total_EXP = 0




for i in range(loop_index):
    EXP_input = input("Enter an option: ")
    # for ambushed 
    if EXP_input == valid_ambushed_inputs[0]:
        total_EXP += ambushed_EXP[0] # increments the EXP amount to the total
    elif EXP_input == valid_ambushed_inputs[1]:
        total_EXP += ambushed_EXP[1]
    elif EXP_input == valid_ambushed_inputs[2]:
        total_EXP += ambushed_EXP[2]
    
    # for normal
    if EXP_input == valid_normal_inputs[0]:
        total_EXP += normal_EXP[0]
    elif EXP_input == valid_normal_inputs[1]:
        total_EXP += normal_EXP[1]
    elif EXP_input == valid_normal_inputs[2]:
        total_EXP += normal_EXP[2]

    # for normal
    if EXP_input == valid_ambushing_inputs[0]:
        total_EXP += ambushing_EXP[0]
    elif EXP_input == valid_ambushing_inputs[1]:
        total_EXP += ambushing_EXP[1]
    elif EXP_input == valid_ambushing_inputs[2]:
        total_EXP += ambushing_EXP[2]

    print(f"Current EXP gained: {total_EXP}")
    

