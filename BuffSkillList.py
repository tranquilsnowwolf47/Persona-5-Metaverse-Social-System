# Filename: BuffSkillList.py
# Date: 2/11/26
# Author: Aoi | shadowsnowwolf
# List of Buff Skills 


class BuffSkills:
    def __init__(self, name, type, SP_cost, description):
        self.name = name
        self.type = type
        self.SP_cost = SP_cost
        self.description = description

    # Shows the full info of the skill
    def display_skill(self):
        print(f"- {self.name} ({self.type})")
        print(f"SP Cost: {self.SP_cost}")
        print(f"Description:\n{self.description}")

class SingularSkills(BuffSkills):
    pass

class AOESkills(BuffSkills):
    pass

# Singular Buff Skills 
confidence_drive = SingularSkills("Confidence Drive", "Atk Buff | Tarukaja effect", 7,
"""   - Embrace your inner confidence, improving your social performance due to your assurance about yourself and your abilities. 
Attack raises temporarily per battle until the effect wears off. Can be stacked and applied again. """)

self_security = SingularSkills("Self-Security", "Def Buff | Rakukaja effect", 7,
"""   - Hone your inner self-security, making yourself unshaken by the opinions, disapproval, or scorn of others. 
You don’t care if others like you– you care about how you view yourself. 
Defense raises temporarily per battle until the effect wears off. Can be stacked and reapplied.""")

slowed_speech = SingularSkills("Slowed Speech", "Ag Buff | Sukukaja effect", 7,
"""   - Slow your verbal tempo which forces you to breathe, choose words deliberately, and leave micro-pauses that let you read reactions and react to unexpected questions or statements in real time. 
You take verbal pauses when needed as well as subtly express to others that you're not in a rush. 
Your social accuracy increases as you trip over your words less and say more of what you meant to say which causes evasion to go up from being less coerced to trip over your words. 
Extremely effective if you typically speak too quickly, stutter a lot, or don’t know what to say right away. 
If you misuse the skill and freeze during an interaction however, it can create awkwardness and tension. 
Accuracy/Evasion raises temporarily per battle until the effect wears off. Can be stacked and reapplied.""")

aura_max = SingularSkills("Aura Max", "Atk + Def + Accuracy/Evasion Buff | Heat Riser effect", 7,
"""   - After building momentum through social warm-ups (multiple low-stakes interactions), you deliberately ignite your inner aura, locking in your activated state. 
Your posture settles, breathing stabilizes, and awareness widens. 
Aura Max converts warm-up momentum into a sustained peak window, causing your presence to become ultra-enhanced-- raising your Attack, Defense, and Accuracy/Evasion temporarily per battle until the effect wears off. 
Confidence becomes steady, composure holds under pressure, and timing sharpens to instinct. 
This skill amplifies existing flow rather than creating it—activating from a cold state has reduced effectiveness and higher strain. Can be stacked and reapplied.""")

three_second_rule = AOESkills("3 Second Rule", "Phys/Gun Attack Buff | Charge effect", 12,
"""   - The moment you spot someone you're drawn to or want you approach, you set a triggered internal countdown. 
Within three seconds, you launch and take action before doubt has time to hijack your thoughts and mind. It's a rapid-fire overdrive that converts hesitation into forward motion. 
Also applies to making decisions where overthinking could creep up if the skill isn’t used. Increases the damage of your next Physical/Gun attack by 2.5x.""")

purpose_focus = AOESkills("Purpose Focus", "Magic Attack Buff | Concentrate effect", 12,
"""   - Before engaging, center yourself by locking in a clear purpose for the interaction, such as seeing if you and the person are compatible, making a potential new friend, networking, trying out a social technique, or simply having a conversation. 
This primes your mindset so you enter with direction instead of hesitation, preventing idle or awkward exchanges. Once the interaction begins, the purpose naturally fades into the background, allowing you to focus on presence, flow, and connection without outcome pressure. 
Your posture, tone, and energy automatically align with your intent, making the approach feel confident and deliberate rather than random. 
Activation Cue: Take three deep breaths, silently repeat, “I am here to [chosen purpose],” and allow the intent to settle into your body language, tone, and energy. 
Increases the damage of your next magic attack by 2.5x.""")


# AOE Buff skills 
pep_talk = AOESkills("Pep Talk", "AOE Atk Buff | Matarukaja effect", 12,
"""   - Rally your friends and boost their confidence, improving your social performance along with theirs due to the belief that you have in one another’s social competence. 
Attack raises temporarily per battle until the effect wears off. Can be stacked and reapplied.""")

collective_closure = AOESkills("Collective Closure Talk", "AOE Def Buff | Marakukaja effect", 12,
"""   - Reassure yourself and your friends of their resilience and mental fortitude to refine their sense of self-security. 
Particularly effective if you or your friends dwell on failure or feel your confidence and self-ability drop. 
Defense raises temporarily per battle until the effect wears off. Can be stacked and reapplied.""")

flow_sync = AOESkills("Flow Sync", "AOE Accuracy/Evasion Buff | Masukukaja effect", 12,
"""   - Remind your friends when they’re speaking too quickly in conversations or brief them/give constructive critique on any verbal or social errors that they’re making. 
This accountability helps them to slow down the cadence of the conversation, boosting their Accuracy/Evasion and yours due to increased situational awareness, increasing conversational flow and speed. 
Use the skill sparingly though, as using it too frequently at once can come across as stepping on toes or overbearing. 
Accuracy/Evasion raises temporarily per battle until the effect wears off. Can be stacked and reapplied.""")

singular_skills = (confidence_drive, self_security, slowed_speech, three_second_rule, purpose_focus)
AOE_skills = (pep_talk, collective_closure, flow_sync)
