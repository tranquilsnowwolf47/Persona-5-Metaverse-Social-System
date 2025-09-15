
def register_persona(name,arcana,level,st,ma,en,ag,lu,skill_one,skill_two,skill_three,skill_four,skill_five,skill_six,skill_seven,skill_eight):
    print("Persona Registered:")
    print(f"Name: {name}")
    print(f"Arcana: {arcana}")
    print(f"Level: {level}\n")
    print("Stats: \n------------------------")
    print(f"St: {st}")
    print(f"Ma: {ma}")
    print(f"En: {en}")
    print(f"Ag: {ag}")
    print(f"Lu: {lu}\n")


    print("Skills:")
    print(f"1. {skill_one}")
    print(f"2. {skill_two}")
    print(f"3. {skill_three}")
    print(f"4. {skill_four}")
    print(f"5. {skill_five}")
    print(f"6. {skill_six}")
    print(f"7. {skill_seven}")
    print(f"8. {skill_eight}")


def register_arsene_build():
    arsene_build = register_persona("Arsene","Fool",15,2,3,7,2,4,"Ignore (Curse)","Request Denial (Curse)","Subject Change (Gun)","Topic Flexbility (Wind)","Prioritized Presence (Curse)","Smile (Fire)","Opinion Challenge (Curse)","Open Ended Question (Wind)")
    return arsene_build

register_arsene_build()

def display_persona():
    result = register_persona()
    return result



#name = str(input("Please enter the name of the Persona to register: "))
#arcana = str(input("Please enter the Arcana of the Persona to register: "))
#level = int(input("Please enter the level of the Persona to register: "))
#st = int(input("Please enter the St stat of the Persona to register: "))
#ma = int(input("Please enter the Ma stat of the Persona to register: "))
#en = int(input("Please enter the En stat of the Persona to register: "))
#ag = int(input("Please enter the Ag stat of the Persona to register: "))
#lu = int(input("Please enter the Lu stat of the Persona to register: "))