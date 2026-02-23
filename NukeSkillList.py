# Filename: NukeSkillList.py
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf
# List of Nuke (Hype Building/Shared Energy) skills from the Metaverse Social System sorted by damage grade 

class NukeSkills:
    def __init__(self, name, element, damage_grade, SP_cost, description):
        self.name = name
        self.element = element
        self.damage_grade = damage_grade
        self.SP_cost = SP_cost 
        self.description = description 

    # Shows the full info of the skill
    def display_skill(self):
        print(f"- {self.name} ({self.element})")
        print(f"SP Cost: {self.SP_cost}")
        print(f"Description:\n{self.description}")

    # Shows the simplified info of the skill
    def display_simplified_info(self):
        print(f"{self.name} ({self.damage_grade} {self.element})")

class SevereSkills(NukeSkills):
    pass

class HeavySkills(NukeSkills):
    pass

class MediumSkills(NukeSkills):
    pass

class LightSkills(NukeSkills):
    pass

example = MediumSkills("X", "Nuke", "Medium", 0,
"""   - X""")

spotlight_surge = HeavySkills("Spotlight Surge", "Nuke", "Heavy", 12,
"""   - Perform a daring or impressive public stunt in an appropriate setting, whether it’s at a convention, event, or social gathering to draw attention and generate hype. 
The act is bold enough to grab eyes, spark conversations, and boost your social presence. 
Timing, confidence, and security in how you may be perceived by others amplify the effect. 
Overdo it, and it can backfire. Using the skill in the wrong setting or during inappropriate scenarios can make you appear cringey or attention-seeking. 
(Ex: When music or a rave is going on at a con, you go in the middle of the crowd and start breakdancing
Ex 2: Showing off a skill or talent publicly in a way that’s exciting or memorable 
Ex 3: Doing a spontaneous dance, pose, or dramatic entrance during a cosplay rave).
Deals heavy Nuke damage.""")

crowd_echo = MediumSkills("Crowd Echo", "Nuke", "Medium", 8,
"""   - You catch onto someone’s excitement and instantly magnify it, bouncing their energy back in a way that amplifies the whole mood. 
Creates a contagious loop of excitement that fuels connection. 
(Ex: Person: “This is the best con I’ve been to!” You: “Right?! The energy here is insane!”
Ex 2: Person: “Dude, that cosplay is fire!” You: “Thanks man! Yours is super clean too!”).
Deals medium Nuke damage. """)

flare_blast = MediumSkills("Flare Blast", "Nuke", "Medium", 9,
"""   - Deliver a high-energy compliment or playful remark that instantly electrifies the target or group. 
Perfect for boosting morale, amplifying excitement, or drawing attention in a way that feels natural and fun.
(Ex: “You really crushed that cosplay! Everyone is noticing!”
Ex 2: “That pose was next-level, I’m lowkey taking notes!”
Ex 3: “Your cosplay makes you look like you came straight out of a cutscene!”).
Deals medium Nuke damage. """)

hyper_link = MediumSkills("Hyper Link", "Nuke", "Medium", 0,
"""   -  Connect multiple people by highlighting shared excitement or achievements, sparking mutual hype. 
By drawing attention to common energy or accomplishments, you strengthen bonds and elevate the group’s mood.
(Ex: “You both made that anime fight look amazing. Could you imagine if the three of us did a collab?” (In the example of a Cloud vs Sephiroth, and you’re a Sora cosplayer for higher chance of success)
Ex 2: “I love how synced you guys are. If we all jumped in, it’d be a highlight of the con for sure”).
Deals medium Nuke damage. """)

sync_surge = MediumSkills("Sync Surge", "Nuke", "Medium", 10,
"""   - When you and another person discover a shared passion or interest, you amplify it by reflecting mutual excitement. 
The energy spreads, boosting both your morale and that of anyone nearby.
(Ex: “Wait, you’re into Kingdom Hearts too? Dude, I’ve gotta hear your favorite boss fight!”
Ex 2: “You regular Megacon each year too?! We totally gotta link up when we see each other again!”).
Deals medium Nuke damage. """)

flash_bounce = MediumSkills("Flash Bounce", "Nuke", "Medium", 9,
"""   - Catch someone’s excitement or hype and bounce it back with equal energy, instantly amplifying the vibe. 
Great for one-on-one or small-group interactions where mirroring enthusiasm sparks connection and spreads positivity. 
(Ex: Person: “Your cosplay is insane!” You: “Thank you so much! Yours is next-level too!”
Ex 2: Person: “I love your keyblade prop!” You: “I love your Scissor Blade prop too! It looks awesome!”).
Deals medium Nuke damage. """)

quick_cheer = LightSkills("Quick Cheer", "Nuke", "Light", 5,
"""   - Give a short, high-energy cheer or reaction that instantly uplifts someone’s mood. Perfect for brief, casual social moments. 
(Ex: “That move was awesome dude!”
Ex 2:  “You nailed that pose!”
Ex 3: “You’re really rocking those shoes!”
Ex 4: “The attention to detail in your cosplay is top-notch”).
Deals light Nuke damage.""")

severe_skill = ()
heavy_skills = (spotlight_surge)
medium_skills = (crowd_echo, flare_blast, hyper_link, sync_surge, flash_bounce)
light_skills = (quick_cheer)
