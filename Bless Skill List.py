# Filename: Bless Skill List.py
# Date: 2/10/26
# Author: Aoi | shadowsnowwolf
# List of Bless skills (Kindness/Warmth)

class BlessSkillls:
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

class SevereSkills(BlessSkillls):
    pass

class HeavySkills(BlessSkillls):
    pass

class MediumSkills(BlessSkillls):
    pass

class LightSkills(BlessSkillls):
    pass

hope_pulse = MediumSkills("Hope Pulse", "Bless", "Medium", 7,
"""   - Share a brief but uplifting perspective that flips negativity into a brighter outlook. 
Used when the mood turns heavy, discouraging, or awkward, this spark of optimism reframes the moment and subtly lifts group dynamics toward positivity. 
The effect works best when it feels genuine and grounded rather than forced.
(Ex 1: Someone: “This project’s a disaster.” You: “Messy projects usually make the best stories once we pull them off.”
Ex 2: Friend: “Feels like I’m failing.” You: “Nah, you’re just mid-upgrade. Every failure’s just the tutorial for your next level.”
Ex 3: Friend after rejection: “Guess I wasn’t good enough.” You: “Or maybe you’re just too good to be stuck in the wrong place. Rejection’s just redirection.”
Coworker: “Man, this meeting was pointless.” You: “Pointless meetings are just practice runs for when we actually get to shine. At least we’re warmed up now. 
Deals medium Bless damage. """)

light_of_insight = MediumSkills("Light of Insight", "Bless", "Medium", 8,
"""   - Offer a perspective that makes obstacles feel manageable, turning worry or hesitation into clarity and hope. 
This skill subtly shifts the mental focus of everyone present toward positive action.
(Ex: “What feels like a dead-end is really just the start of the next chapter.”
Ex 2: “These challenges are stepping stones you didn’t know you had.”
Ex 3: “This obstacle is tricky, but you’ve handled tougher before. Trust yourself.”
Ex 4: “You’ve got the skills to figure this out. Sometimes you just need a fresh perspective.’
Ex 5: “It’s okay to stumble. Each step forward counts, even if it’s small.”
Deals medium Bless damage. """)

heartfelt_thanks = MediumSkills("Heartfelt Thanks", "Bless", "Medium", 7,
"""   - Acknowledge and celebrate someone’s effort in connecting, no matter how awkward or inexperienced they are. 
Your sincere recognition makes them feel valued, builds confidence, and encourages future attempts at social engagement. Also applies to when someone approaches you. 
(Ex: “Hey, that was really kind of you to say! I appreciate it!”
Ex 2: “It might have felt a little awkward, but that effort really made my day”
Ex 3: “I can tell you tried. Thank you, it means a lot”
Ex 4: “It meant a lot that you approached me”
Ex 5: “Thanks a lot for approaching me! It was a lot of fun talking with you”).
Deals medium Bless damage. """)

benevolence_ray = MediumSkills("Benevolence Ray", "Bless", "Medium", 7,
"""   - Share an observation about the target’s behavior, demeanor, or choices that frames them in a positive light they might not have considered themselves. 
It’s a subtle reminder of their worth, often catching them pleasantly off guard and opening space for more meaningful connection. 
Ex: Your friend goes for someone’s number but the person doesn’t give it to them, and you praise their courage for approaching regardless.  
Ex 2: Your friend beats themselves up for not seeing results, but you highlight to them how unrecognizably focused they’ve been the past few months. 
Ex 3: A friend comments on how they felt awkward or socially off and you highlight that most people don’t notice what you’re stressing about and don’t care as much as you think they do.
Deals medium Bless damage.""")

gentle_push = LightSkills("Gentle Push", "Bless", "Light", 4,
"""   - Warmly encourage the target to take a small leap. 
The support is lighthearted but targeted, designed to make participation feel safe and supportive, rather than intimidating. 
Perfect for moments where a little confidence boost can spark action. 
(Ex: You should give it a shot. I’ll be cheering you on”
Ex 2: “One small step and you’ll see it’s not so scary after all”
Ex 3: “Why not give this a shot sometime? You won’t regret it”)
Ex 4: “You don’t have to be perfect. Just give it a shot”.
Ex 5: “You should ask them if you have a question. Go for it.”
Ex 6: “If you give it a shot, it might be something you actually really enjoy”).
Deals light Bless damage.""")

sunbeam_remark = LightSkills("Sunbeam Remark", "Bless", "Light", 5,
"""   - Deliver a brief, radiant compliment that casts someone in a warm and positive light, like a spotlight that subtly lifts the atmosphere. 
The intent is to make the person feel like they stand out and that they feel unique, impressive, or exceptional in the moment. 
Works best when the compliment is specific, sincere, and casually delivered. 
(Ex 1: “The way you explain things is much different than the orthodox way of teaching.”
Ex 2: “I can really see the confidence you have when you walk into a room”
Ex 3: “You have a very natural way of speaking”
Ex 4: “You’ve got a really magnetic presence in the way you speak”
Ex 5: “Your energy really brightens the room”).
Deals light Bless damage.""")

encouraging_boost = LightSkills("Encouraging Boost", "Bless", "Light", 4,
"""   - Offer a timely spark of support while someone’s in the middle of their effort. 
The encouragement validates their progress and fuels momentum, lifting their morale without sounding forced. Works best when it’s specific and in-the-moment, so they feel seen and energized rather than flattered. 
It inspires the person to keep going and validates their efforts.
(Ex: “You’re actually killing it right now, keep going!”
Ex 2: “You’re super locked in right now, keep up the good work!”
Ex 3: “You’ve already pushed through the hardest part, finish strong!”
Ex 4: “You’re doing better than you realize.”
Ex 5: “That looked like a pretty good form to me.”
Ex 6: “That adjustment you made is really working.”
Ex 7: “Let’s go, you got 2 more reps! Finish strong!”
Ex 8: “You’re a lot more focused than you think. Just look at the progress you’ve been making”).
Deals light Bless damage.""")

warm_smile = LightSkills("Warm Smile", "Bless", "Light", 4,                    
"""   - A deliberate, heartfelt smile paired with steady eye contact. 
Rather than just being nice, it’s a signal that says you’re welcome here, disarming social tension and creating a micro-moment of trust in the middle of the exchange. 
Deals light Bless damage.""")

gracious_thanks = LightSkills("Gracious Thanks", "Bless", "Light", 0,
"""   - When someone offers you a compliment, you respond with warm gratitude that magnifies the positivity of the moment. 
Rather than brushing it off or downplaying it, you acknowledge their kindness and make them feel good for expressing it. 
This simple thank-you creates a ripple of optimism that lingers. 
(Ex: ”Thanks, that really means a lot coming from you.”
Ex 2: ”I appreciate that. That made my day.
Ex 3: ”Thank you, that was really kind of you to say”
Ex 4: “I really appreciate you saying that.”).
Deals light Bless damage.""")
