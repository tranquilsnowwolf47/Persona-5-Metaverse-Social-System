def buildPersona(persona_name,persona_arcana,persona_level, st, ma, en, ag, lu):
    print(f"Name: {persona_name}")
    print(f"Arcana: {persona_arcana}")
    print(f"Level: {persona_level}\n")

    print(f"St: {st}")
    print(f"Ma: {ma}")
    print(f"En {en}")
    print(f"Ag {ag}")
    print(f"Lu: {lu}\n")
    print("--------------------------------")



p1 = buildPersona("Arsene","Fool",12,2,2,5,2,4)
p2 = buildPersona("Jack-o'-lantern","Magician",1,1,1,1,1,1)
p3 = buildPersona("Silky","Priestess",1,1,1,1,1,1,)
p4 = buildPersona("Eligor","Emperor",1,1,1,1,1,1)


# Can hold up to eight skills per Persona
def givePersonaSkills(skill_one,skill_two,skill_three,skill_four,skill_five,skill_six,skill_seven,skill_eight):
    print("Skills:\n-----------------------------")


arsene_skills = givePersonaSkills("Ignore (Curse)","Request Denial (Curse)","Subject Change (Gun)","Topic Flexibility (Gun)","Prioritize Prescence (Psy)")
jack_o_lantern_skills = givePersonaSkills("Curiousity (Wind)","Common Interest (Wind)","Open Ended Question (Wind)")
silky_skills = givePersonaSkills("Shadow Read (Psy)","Obs","")
eligor_skills = givePersonaSkills("","","")