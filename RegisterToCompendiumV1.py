# Filename: RegisterToCompendiumV1.py
# Date: 9/17/25
# Author: Aoi | shadowsnowwolf

# Note: Beta version of the compendium registration feature
# This specifically registers Personas to the compendium
# For the final, large program, import this as a module feature with a menu for the choices 
# File will be named VelvetRoom.py


class Compendium:
    def register_persona(self,f, name,arcana,level,st,ma,en,ag,lu,skill_one,skill_two,skill_three,skill_four,skill_five,skill_six,skill_seven,skill_eight):
        print("Persona Registered:", file=f)
        print(f"Name: {name}", file=f)
        print(f"Arcana: {arcana}", file=f)
        print(f"Level: {level}\n", file=f)
        print("Stats: \n------------------------", file=f)
        print(f"St: {st}", file=f)
        print(f"Ma: {ma}", file=f)
        print(f"En: {en}", file=f)
        print(f"Ag: {ag}", file=f)
        print(f"Lu: {lu}\n", file=f)

        print("Skills:", file=f)
        print(f"1. {skill_one}", file=f)
        print(f"2. {skill_two}", file=f)
        print(f"3. {skill_three}", file=f)
        print(f"4. {skill_four}", file=f)
        print(f"5. {skill_five}", file=f)
        print(f"6. {skill_six}", file=f)
        print(f"7. {skill_seven}", file=f)
        print(f"8. {skill_eight}", file=f)
        print("\n", file=f)

    # Fool Personas:
    # ------------------------------------------------------------------------------------
    # 1. Arsene
    def register_arsene_build(self,f):
            return self.register_persona(
                f, 
                "Arsene","Fool",28,
                7,8,7,7,4,
                "Slowed Speech (Ag Buff)","3 Second Rule (Charge)","Ether Break (Atk debuff)",
                "Minimum Echo (Med Curse)","Data Hex (Med Curse)","Decision Strike (Med Phys)",
                "Assertive Slice (Med Phys)","Shadow Read (Hvy Psy)"
            )
        
    # 2. Obariyon
    def register_obariyon_build(self,f):
            return self.register_persona(
                # Register update: 9/15/25
                # Register update 10/4/25
                f,
                "Obariyon","Fool",31,
                9,7,7,5,7,
                "Mind Glide (Med Wind)","Deep Dive (Med Wind)","Interest Probe (Med Gun)",
                "Shocking Humor (Light Elec)","Crowd Echo (Med Nuke)","Sync Surge (Med Nuke)",
                "Human Nature Savant (Auto Ag Buff)","Looksmax (Auto Heat-Riser)"
            )
        
    # 3. Orpheus F
    def register_orpheus_f_build(self,f):
            # Register update: 11/17/25
            # Register update 12/17/25
            return self.register_persona(
                f,
                "Orpehus F", "Fool", 29,
                8,6,7,7,4,
                "Act Sense (Med Psy)","Tranquil Edge (Med Psy)","Ether Break (Atk debuff)","Volt Nudge (Light Elec)",
                "Clock Hold (Med Curse)","Hidden Blueprint (Med Curse)","Data Hex (Med Curse)","Minimum Echo (Med Curse)"
            )


    # Magician Personas:
    # ------------------------------------------------------------------------------------
        # 1. Jack-o'-lantern 
    def register_jack_o_lantern_build(self,f):
            # Register update: 9/14/25
            return self.register_persona(
                f, 
                "Jack-o'-Lantern", "Magician",20,
                4,10,5,3,2,
                "Winds of Knowledge (Medium Wind)","Career Current (Medium Wind)","Deep Dive (Medium Wind)","Mind Glide (Medium Wind)","Subject Shift (Light Gun)",
                "Mini-Talk (Light Gun)","Echo Shot (Light Gun)","Velvet Note (Medium Fire)")

    # 2. Cait Sith
    def register_cait_sith_build(self,f):
            return self.register_persona(
                f,
                "Cait Sith", "Magician", 21,
                3,9,5,6,1,
                "","","","","","","",""
        )

    # 3. Jack Frost
    def register_jack_frost_build(self,f):
           return self.register_persona(
                  # Register Update: 12/17/25
                  f,
                  "Jack Frost", "Magician",
                  5,10,5,5,1,
                 "","","","","","","",""
           )

    # Priestess Personas:
    # ------------------------------------------------------------------------------------
    # 1. Silky
    def register_silky_build(self,f):
            return self.register_persona(
                f, 
                "Silky","Priestess",17,
                2,10,6,6,1,
                "Shadow Read (Hvy Psy)","Temperament Read (Light Psy)","Environment Scan (Med Psy)",
                "Observation (Light Psy)","Extraction Shot (Light Gun)","Small-talk (Light Gun)","Reassuring Chill (Light Ice)",
                "Slowed Speech (Ag Buff)"
            )
        
    # 2. Apsaras
    def register_apsaras_build(self,f):
            return self.register_persona(
                # Register update: 9/29/25
                f,
                "Apsaras","Priestess",29,
                2,10,8,10,4,
                "Shadow Read (Hvy Psy)","Temperament Read (Light Psy)","Environment Scan (Psy)","Observation (Light Psy)","","","Reassuring Chill (Ice)","Slowed Speech (Ag Buff)"
            )

    # 3. Koh-i-Noor
    def register_koh_i_noor_build(self,f):
           return self.register_persona(
                  f,
                  "Koh-i-Noor","Priestess",8,
                  1,3,3,4,1,
                  "","","","","",
                  "","","",
           )


    # Emperor Personas:
    # ------------------------------------------------------------------------------------
    # 1. Eligor
    def register_eligor_build(self,f):
            return self.register_persona(
                f, 
                "Eligor", "Emperor",24,
                10,5,7,3,5,
                "Assertive Slice (Phys)","Request Denial (Curse)","Name Repeat (Psy)","Extraction Shot (Gun)","","","",""
            )
        
    # 2. Regent
    def register_regent_build(self,f):
        # Register update: 8/31/25
            return self.register_persona(
                # Register update: 9/15/25
                # Register update: 10/4/25
                f,
                "Regent", "Emperor", 28,
                13,6,10,2,1,
                "Assertive Slice (Med Phys)","Stonewall (Med Phys)","Decision Strike (Med Phys)","Cold Cut (Med Phys)",
                "Magnetic Aura (Med Fire)","Verbal Parry (Med Elec)","3 Second Rule (Charge)","Rhythm Break (Ag Debuff)"
            )

    # 3. Setanta
    def register_setanta_build(self,f):
        # Register update: 11/17/25
        f,
        "Setanta", "Emperor", 23,
        11,5,8,2,1
        "Assertive Slice (Med Phys)", "Stonewall (Med Phys)", "Decision Strike (Med Phys)", "Calling Fang (Med Phys)", 
        "Magnetic Aura (Med Fire)","Verbal Parry (Med Elec)", "3 Second Rule (Charge)"

    # Hermit Personas:
    # ------------------------------------------------------------------------------------
    # 1. Bicorn
    def register_bicorn_build(self,f):
            return self.register_persona(
                f,
                "Bicorn", "Hermit",16, 
                1,6,6,1,7,
                "Cooldown (Ice)", "Prioritized Presence (Med Psy)","Soulshare (Ice)","Empathic Echo (Ice)","Reassuring Chill (Ice)","","",""
            )

    # Death Personas:
    # ------------------------------------------------------------------------------------
    # 1. Mandrake
    def register_mandrake_build(self,f):
            return self.register_persona(
                f,
                "Mandrake", "Death", 20,
                2,4,7,5,7,
                "Slowed Speech (Ag buff)","Self-Control (Auto-Def buff)","Self-Security (Def buff)",
                "Confidence (Atk buff)", "3 Second Rule (Charge)", "", "", ""
            )
        
    # 2. Mokoi
    def register_mokoi_build(self,f):
            # Register udpate: 9/15/25
            return self.register_persona(
                f,
                # Register update: 10/4/25
                "Mokoi","Death", 27,
                1,9,9,8,4,
                "Slowed Speech (Ag buff)","Self-Control (Auto Def buff)","Self-Security (Def buff)",
                "Confidence (Atk buff)","Act Sense (Med Psy)","Tranquil Edge (Med Psy)","Hollow Stance (Light Curse)","Minimum Echo (Med Curse)"
            )

    # Strength Personas:
    # ------------------------------------------------------------------------------------
    # 1. Kelpie
    def register_kelpie_build(self,f):
            return self.register_persona(
                f,
                "Kelpie", "Strength", 16,
                6,3,7,1,2,
                "","","","","","","",""
            )
        
    # 2. Shiisaa
    def register_shiisaa_build(self,f):
            return self.register_persona(
                # Register update: 10/4/25
                f,
                "Shiisaa", "Strength", 21,
                5,4,11,3,2,
                "","","","","","","",""
            )
    
    # 3. Oni
    def register_oni_build(self,f):
           return self.register_persona(
                  # Register update: 11/17/25
                  f,
                  "Oni","Strength", 15,
                  5,2,9,1,2,
                  "","","","","","","", "Self-Control (Auto Def buff)"
           )

    # Lovers Personas:
    # ------------------------------------------------------------------------------------
    # 1. Pixie
    def register_pixie_build(self,f):
            return self.register_persona(
                f,
                "Pixie", "Lovers", 19,
                1,7,4,5,5,
                "Self Respect Affirmation","Prioritized Presence (Med Psy)","Nonchalance (Med Psy)","Interest Level Read (Light Psy)","","","",""
            )
    # 2. Saki Mitama
    def register_saki_mitama_build(self,f):
            return self.register_persona(
                # Register update: 10/4/25
                f,
                "Saki Mitama","Lovers",25,
                7,8,3,6,6,
                "Focused Breathing (Lvl 1 Healing)", "Cat Nap (Lvl 2 Healing)","","","","","",""
            )
    # 3. Ame-no-Uzume
    def register_ame_no_uzume_build(self,f):
           return self.register_persona(
                  # Register update: 11/17/25
                  f,
                  "Ame-no-Uzume", "Lovers",17,
                  4,8,3,2,4,
                  "Focused Breathing (Lvl 1 Healing)","Cat Nap (Lvl 2 Healing)","","","","","",""
           )

    # Chariot Personas:
    # ------------------------------------------------------------------------------------
    # 1. Agathion
    def register_agathion_build(self,f):
            return self.register_persona(
                f, 
                "Agathion","Chariot", 20,
                5,4,5,3,2,
                "Self-Control","Gentleman's Flattery","Direct Curiosity","","","","",""
            )
        
    # 2. Slime
    def register_slime_build(self,f):
            # Register update: 9/15/25
            return self.register_persona(
                f,
                # Register update: 9/15/25
                "Slime","Chariot", 20,
                7,5,5,4,1,
                "Sync surge (Med Nuke)","Hyper Link (Med Nuke)","Flare Blast (Med Nuke)","3 Second Rule (Charge)",
                "Confidence (Atk Buff)","Opening Gambit (Hvy Phys)","Calling Fang (Med Phys)","Brain Flicker (Med Elec)"
            )

    # Justice Personas:
    # ------------------------------------------------------------------------------------
    # 1. Angel
    def register_angel_build(self,f):
            return self.register_persona(
                f,
                # Register update: 10/4/25
                "Angel","Justice", 27,
                4,6,6,6,5,
                "","","","","","","",""

            )

    # Hanged Man Personas:
    # ------------------------------------------------------------------------------------
    # 1. Hua Po
    def register_hua_po_build(self,f):
            return self.register_persona(
                f,
                "Hua Po","Hanged Man", 17,
                6,4,8,1,1,
                "Prioritized Presence,","Slowed Speech","Echo Shot","Casual Greeting Shot","Small-talk","Subject Change","Interest Probe",""
            )

    # Fortune Personas:
    # ------------------------------------------------------------------------------------
    # 1. Stone of Scone
    def register_stone_of_scone_build(self,f):
            return self.register_persona(
                f,
                "Stone of Scone", "Fortune", 13,
                1,1,3 ,3,6,
                "Social Competence","Interest Level Read","","","","","",""
            )

    # Empress Personas:
    # ------------------------------------------------------------------------------------
    # 1. Queen's Necklace
    def register_queens_necklace_build(self,f):
            return self.register_persona(
                f,
                "Queen's Necklace","Empress", 16,
                5,4,3,6,3,
                "Temperament Read","","","","","","",""
            )

    # Sun Personas:
    # ------------------------------------------------------------------------------------
    # 1. Suzaku
    def register_suzaku_build(self,f):
            return self.register_persona(
                # Register update: 10/4/25
                # Register update: 11/17/25
                f,
                "Suzaku", "Sun", 23,
                7,8,5,3,4,
                "Ember Gaze (Med Fire)","","","","Looksmax (Auto Heat-Riser)","Confidence (Atk buff)","Social Competence (Auto Atk Buff)",
                "Ascendancy Wave (AOE Ag Debuff)"
            )

    
   # Faith Personas:
   # ------------------------------------------------------------------------------------
   # 1. Phoenix
    def register_phoenix_build(self,f):
           return self.register_persona(
            # Register update: 11/17/25
            f,
            "Phoenix","Faith",11,
            3,1,3,1,2,
            "","","","","","","",""

           )


comp = Compendium()
with open("Persona_compendium_logbook.txt", "a") as file:
    # Fool Personas
    comp.register_arsene_build(file)
    comp.register_obariyon_build(file)
    comp.register_orpheus_f_build(file)

    # Magician Personas
    comp.register_cait_sith_build(file)
    comp.register_jack_o_lantern_build(file)
    comp.register_jack_frost_bulid(file)

    # Priestess Personas
    comp.register_silky_build(file)
    comp.register_apsaras_build(file)
    comp.register_koh_i_noor_build(file)

    # Empress Personas
    comp.register_queens_necklace_build(file)

    # Emperor Personas
    comp.register_eligor_build(file)
    comp.register_regent_build(file)
    comp.register_setanta_build(file)
    
    # Hermit Personas
    comp.register_bicorn_build(file)

    # Death Personas
    comp.register_mokoi_build(file)
    
    
    # Chariot Personas
    comp.register_agathion_build(file)
    comp.register_slime_build(file)

    # Lovers Personas
    comp.register_pixie_build(file)
    comp.register_saki_mitama_build(file)
    comp.register_ame_no_uzume_build(file)

    # Hanged Man Personas
    comp.register_hua_po_build(file)

    # Death Personas
    comp.register_mandrake_build(file)

    # Strength Personas
    comp.register_kelpie_build(file)

    # Justice Personas
    comp.register_angel_build(file)

    # Fortune Personas
    comp.register_stone_of_scone_build(file)

    # Sun Personas
    comp.register_suzaku_build(file)

    # Faith Personas
    comp.register_phoenix_build(file)
    


    #def display_persona():
        #result = Compendium.register_persona()
        #return result



#name = str(input("Please enter the name of the Persona to register: "))
#arcana = str(input("Please enter the Arcana of the Persona to register: "))
#level = int(input("Please enter the level of the Persona to register: "))
#st = int(input("Please enter the St stat of the Persona to register: "))
#ma = int(input("Please enter the Ma stat of the Persona to register: "))
#en = int(input("Please enter the En stat of the Persona to register: "))
#ag = int(input("Please enter the Ag stat of the Persona to register: "))


#lu = int(input("Please enter the Lu stat of the Persona to register: "))
