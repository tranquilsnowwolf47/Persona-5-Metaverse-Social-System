# Filename: Psy Skill List.py
# Date: 2/7/26
# Author: Aoi | shadowsnowwolf
# List of Psy skills (Mind reading/Psychological perception)

class PsySkills:
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

class SevereSkills(PsySkills):
    pass

class HeavySkills(PsySkills):
    pass

class MediumSkills(PsySkills):
    pass

class LightSkills(PsySkills):
    pass

# Heavy Skills 
shadow_talk = HeavySkills("Shadow Talk", "Psy", "Heavy", 14,
"""   - Step back and let the target expose their inner self, including their repressed thoughts and hidden desires. By observing without interference, you gain deep insight into their true intentions, fears, and vulnerabilities, revealing patterns they may not even be consciously aware of. This allows you to anticipate reactions, exploit weaknesses, and plan your next move with precision. The skill transforms subtle cues into actionable information, giving you a clear strategic advantage.
Ex: Watching someone react to another person’s success or failure, you notice a fleeting expression of envy or frustration. Shadow Talk uncovers a fear of being left behind or alone.
Ex 2: A person overreacts to a comment about their past. Shadow Talk lets you see the repressed trauma or insecurity driving their actions. 
Ex 3: In a conversation, someone puts you down and makes you sound like you’re inferior. Shadow Talk reveals that the person may have a superiority complex. 
Deals heavy Psy damage.""")

cognition_rift = HeavySkills("Cognition Rift", "Psy", "Heavy", 12,
"""   - Instead of listening to what someone says, you pay attention to their actions instead, allowing you to notice the subtle patterns, the effort they actually put in, the consistency of their actions, and the truth behind how authentic and genuine they really are . Cuts through excuses, fluff, and flaking, giving you a clear read on whether they’ll follow through or if they are who they say they are. 
(Ex: Someone promises to meet up but consistently flakes
 Ex 2: A new acquaintance claims that they care, but their actions show little intention on following through
 Ex 3: A family member or romantic interest claims to love you, but they disrespect and take advantage of you
 Ex 4: Someone constantly texts but never follows through with actions (i.e., sending memes but skipping real meetups)
 Ex 4: They compliment you and flirt, but avoid making time for you or cancels plans).
Deals heavy Psy damage. """)

prioritized_presence = HeavySkills("Prioritized Presence", "Psy", "Heavy", 12,
"""   - Hold your ground and let incoming dms/plans wait in your inbox, signaling that your time and attention are valuable. 
You can do this by getting genuinely busy rather than sitting and waiting a certain amount of time to respond. 
By responding on your own schedule, you create mystery, signal to others that your personal time has priority, and may generate the scarcity effect in your target conveying yourself as more valuable through intentional space. 
Reinforces emotional balance, reduces the chance of over-investment, and conveys to your target that you have a life and that you’re not afraid to set boundaries with your time when you need to. 
By taking advantage of the psychological idea that scarcity creates value, you build intrigue and a desire to know more within the target Shadow. 
This skill is only effective once you build rapport with the target however– it isn’t very effective against Shadows that don’t care or don’t really know you. 
Deals heavy Psy damage.""")


# Medium Skills 
soulstring_pull = MediumSkills("Soulstring Pull", "Psy", "Medium", 8,
"""   - Trigger an emotional response by striking a psychological chord with the target. 
Evoke nostalgia, excitement, or defensiveness to reveal their Shadow type, build rapport, or manipulate reactions. 
Misreading the cue may cause brief awkwardness. Deals medium Psy damage.""")

atmosphere_read = MediumSkills("Atmosphere Read", "Psy", "Medium", 7,
"""   - Heighten your psychological perception to read the environment and underlying dynamics of any situation. 
Detect conflicts, opportunities, or the flow of interactions to strategically plan your next move or skill use. 
Deals medium Psy damage.""")

atmos_gauge = MediumSkills("Atmos Gauge", "Psy", "Medium", 7,
"""   - Read the room through psychological perception to sense the social mood, dynamics, receptiveness of those around you, and perceived risk of engagement or certain behaviors. 
Helps determine whether an encounter, approach, or action is appropriate, and guides how to act without causing friction or unnecessary risk. 
Deals medium Psy damage.""")

tranquil_edge = MediumSkills("Tranquil Edge", "Psy", "Medium", 7,
"""   - Maintain a calm and collected demeanor, putting the ball in your court and giving yourself leverage to not chase/over-invest during interactions. 
By showing that you're not going to crack under pressure to people's temperaments, you show your high value and earn respect. 
Staying nonchalant is also effective against problematic people that want to initiate arguments. 
When you show that you're not willing to entertain someone’s problematic behavior, it may negate/dispel their energy entirely. 
Deals medium Psy damage.""")

energy_mirror = MediumSkills("Energy Mirror", "Psy", "Medium", 7,
"""   - Subtly mirror the other person's pace, tone, and body language, matching their energy level. 
By aligning your own emotional rhythm to theirs, you create an automatic bond: they feel understood without realizing why. 
This resonance lowers their social guard, smooths the flow of the conversation, and boosts the effectiveness of follow up skills. 
Deals medium Psy damage.""")

kinesis_gap = MediumSkills("Kinesis Gap", "Psy", "Medium", 8,
"""   - Deliberately reduce your own conversational effort and level of engagement in the conversation, putting noticeably less effort to create a control factor where the target’s natural behavior becomes easier to read. 
By stepping back emotionally and verbally, you remove your influence from the interaction, revealing the target’s true communication style, interest level, and investment to emerge without distortion or personal bias. 
This skill gives you valuable insight on the target’s character and social patterns without overly testing them or applying pressure. 
Deals medium Psy damage.""")


# Light Skills 
interest_gauge = LightSkills("X", "Psy", "Light", 5,
"""   - Dial into micro-cues, response latency, eye contact, verbal tone, body language, investment level, and response quality to categorize the target's true investment as high, medium, or low interest. 
Helps you avoid wasted energy on disinterested parties and give further clarity on whether to continue the interaction or to go for an All-Out Attack. 
Can be effective with determining whether someone wants to continue in conversation with you or is secretly reserved. 
Deals light Psy damage.""")

temperament_read = LightSkills("X", "Psy", "Light", 5,
"""   - Quickly assess the target’s temperament based on their person's overall vibe and first few behaviors-- friendly, calm, tense, charismatic, playful, irritable, etc. 
By scanning the target, this reveals their dominant temperament, highlights psychological openings or weaknesses, and gives you an idea on how to proceed or what mask to switch to (if Wild Card or more than one Persona). 
This can help you determine what their weakness is as well as their elemental affinities and resistances are. 
Deals light Psy damage.""")

love_interpreter = LightSkills("X", "Psy", "Light", 5,
"""   - Tune in and analyze how someone naturally gives and receives care– how they respond to compliments, when you spend time with them,  physical closeness, gifts, etc. 
Through these means, you're able to pinpoint their primary love language (Words of Affirmation, Quality Time, Gifts, Acts of Service, or Physical Touch), tagging it in your mind. 
Armed with this insight, your next Fire, Ice, Wind or Bless skill can lead to a technical and deal extra damage. 
Deals light Psy damage.""")

sixth_observation = LightSkills("X", "Psy", "Light", 5,
"""   - Generally scan the target internally, reading their micro-behaviors, tone shift, tone, posture, and subtle cues to gather psychological information. 
It sharpens your awareness, revealing small details that can influence your next move. 
(I.e., noticing someone looks disinterested from their body language, noticing that someone looks nervous or uncomfortable, noticing when someone is starting to get emotional after a certain topic gets brought up by their facial expression and demeanor, spotting hesitation before they answer). 
Deals light Psy damage. """)

name_echo = LightSkills("X", "Psy", "Light", 5,
"""   - Intentionally use the person’s name during conversation to trigger their natural attention response, sharpen your read on them, and commit their name to memory to increase your chances of remembering it. 
This skill takes advantage of the psychological idea that humans are wired to orient towards their name. 
Repeating someone's name activates parts of the brain tied to attention and reward, and can make them feel more seen and validated like you’re truly noticing them, which instantly ramps up rapport and trust, on top of making you look more attentive and considerate in future interactions.
Ex 1: “So Mateo… you said you’re studying comp sci right?”
Ex 2 :”I’m looking forward to seeing you again soon Catherine”
Ex 3: “It’s okay to be nervous Aiden. It’s just part of the experience”).
Deals light Psy damage.""")

severe_skills = ()
heavy_skill = (shadow_talk, cognition_rift, prioritized_presence)
medium_skills = (soulstring_pull, atmosphere_read, atmos_gauge, tranquil_edge, energy_mirror, kinesis_gap)
light_skills = (interest_gauge, temperament_read, love_interpreter, sixth_observation, name_echo)
