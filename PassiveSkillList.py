# Filename: PassiveSkillList.py
# Date: 2/19/26
# Author: Aoi | shadowsnowwolf
# List of Passive Skills 


class PassiveSkillList:
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

    # Shows info for the skill (if it doesn't have an SP cost)
    def display_skill2(self):
        print(f"- {self.name} ({self.type})")
        print(f"Description:\n{self.description}")



example = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - X""")


class AffinityPassiveSkills(PassiveSkillList):
    pass

class PassiveSkills(PassiveSkillList):
    pass

class StatusAilmentPassiveSkills(PassiveSkillList):
    pass


# Affinity Passive Skills 
dodge_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Phys (Bluntness / Assertiveness) attacks. 
Direct challenges, hard checks, and confrontational pressure are recognized early, allowing you to delay, redirect, or soften them before they fully land.""")
    
dodge_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Gun (Low Risk / Light Probing) attacks. 
Casual questions, value tests, and surface-level probes are recognized early, allowing you to pause, redirect, or give non-committal responses before any leverage is gained.""")
    
dodge_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Fire (Charm / Charisma) attacks. 
Playful teasing, flirting, confident compliments, and magnetic presence are recognized early, allowing you to pause, redirect, or cool the interaction before charm can influence your emotions or decisions.""")
    
dodge_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Ice (Emotional Control / Emotional Maneuvering) attempts. 
Emotional validation, mirroring, and subtle emotional pacing are recognized early, allowing you to delay or redirect before your emotional state or tempo is guided.""")
    
dodge_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Elec (Wit / Humor) disruption. 
Clever jokes, wordplay, and playful jabs are noticed early, allowing you to prevent humor from interrupting your timing, confidence, or conversational rhythm.""")
    
dodge_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Wind (Curiosity / Connection) pulls. 
Thoughtful questions, rapport-building prompts, and conversational flow are recognized early, allowing you to pause or redirect before your attention, focus, direction, or disclosures are subtly guided.""")
    
dodge_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Psy (Mind Reading / Psychological Perception) pressure. 
Psychological reads, pattern recognition, and insight-based observations are noticed early, allowing you to slow the interaction before those reads can be leveraged.""")
    
dodge_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Nuke (Hype Building / Shared Energy) surges.
Collective enthusiasm, mirrored excitement, and momentum are recognized early, allowing you to delay engagement before energy can rush decisions or actions.""")
    
dodge_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Bless (Kindness / Warmth) influence. 
Encouragement, positivity, and sincere goodwill are recognized early, allowing you to pause and reflect before warmth subtly shapes expectations, emotions, or choices.""")
    
dodge_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Curse (Unconventional Moves / Unorthodoxy) pressure. 
Bold truth drops, self-deprecating remarks, risky or uncomfortable moves, and sudden frame shifts are recognized early, allowing you to pause, ground yourself, or redirect before discomfort or disruption can knock you off balance.""")

dodge_reverse_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Phys (Aggression / Intimidation) pressure. 
Ego-driven dominance, raised voices, and coercive energy are recognized early, allowing you to pause, reframe, or slow the exchange before intimidation can create fear, submission, or escalation.""")
    
dodge_reverse_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Gun (Nosiness / Prying) attempts. 
Intrusive questions and boundary-testing probes are noticed early, allowing you to delay, redirect, or respond non-committally before any leverage is gained.""")
    
dodge_reverse_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Fire (Seduction / Validation) pressure. 
Performative charm, flattery traps, and attention bait are recognized early, allowing you to cool the interaction before ego pull, attraction bias, or obligation can form.""")
    
dodge_reverse_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Ice (Hyperemotionality / Emotional Disregulation) pressure. 
Emotional flooding, guilt spirals, and volatile displays are noticed early, allowing you to slow, ground, or redirect before overwhelming or caretaking pressure sets in.""")
    
dodge_reverse_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Elec (Mockery / Ridicule) attempts. 
Mean-spirited humor, sarcastic digs, and public jabs are recognized early, allowing you to disengage or slow the moment before embarrassment or provocation can land.""")
    
dodge_reverse_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Wind (Conversational Steering / Feigned Interest) pressure. 
Leading questions and performative listening are detected early, allowing you to pause or redirect before your attention or conclusions are subtly guided.""")
    
dodge_reverse_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Psy (Psychological Manipulation / Emotional Exploitation) pressure. 
Frame hijacks, guilt framing, and covert psychological tactics are noticed early, allowing you to slow the interaction before perception or decisions can be distorted.""")
    
dodge_reverse_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Nuke (Impulsivity / Overstimulation) pressure. 
Chaotic hype, urgency, and emotional overload are recognized early, allowing you to slow pacing before overwhelm or impulsive action is triggered.""")
    
dodge_reverse_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Bless (Ingenuine Kindness / Sincerity Facade) pressure. 
Performative warmth and fake positivity are recognized early, allowing you to pause before obligation, guilt, or trust shifts can form.""")
    
dodge_reverse_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Curse (Behavioral Corruption / Doubt Leverage) pressure. 
Subtle discouragement and hesitation-seeding are recognized early, allowing you to pause and reaffirm direction before doubt can slow action.""")


# Passive Skills
diamond_mirror = 
aegis_mirror =
regenerate_I =
regenerate_II =
regenerate_III =
invigorate_I =
invigorate_II =
invigorate_III =
gun_boost = 
fire_boost =
ice_boost =
elec_boost =
wind_boost =
psy_boost =
nuke_boost =
bless_boost =
curse_boost =

gun_amp = 
fire_amp =
ice_amp =
elec_amp =
wind_amp =
psy_amp =
nuke_amp =
bless_amp =
curse_amp =
