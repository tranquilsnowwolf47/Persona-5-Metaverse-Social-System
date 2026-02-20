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
# ------------------------------------------------------------------------
# Dodge skills 
dodge_phys = AffinityPassiveSkills("Dodge Phys", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Phys (Bluntness / Assertiveness) attacks. 
Direct challenges, hard checks, and confrontational pressure are recognized early, allowing you to delay, redirect, or soften them before they fully land.""")
dodge_gun = AffinityPassiveSkills("Dodge Gun", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Gun (Low Risk / Light Probing) attacks. 
Casual questions, value tests, and surface-level probes are recognized early, allowing you to pause, redirect, or give non-committal responses before any leverage is gained.""")
dodge_fire = AffinityPassiveSkills("Dodge Fire", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Fire (Charm / Charisma) attacks. 
Playful teasing, flirting, confident compliments, and magnetic presence are recognized early, allowing you to pause, redirect, or cool the interaction before charm can influence your emotions or decisions.""")
dodge_ice = AffinityPassiveSkills("Dodge Ice", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Ice (Emotional Control / Emotional Maneuvering) attempts. 
Emotional validation, mirroring, and subtle emotional pacing are recognized early, allowing you to delay or redirect before your emotional state or tempo is guided.""")
dodge_elec = AffinityPassiveSkills("Dodge Elec", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Elec (Wit / Humor) disruption. 
Clever jokes, wordplay, and playful jabs are noticed early, allowing you to prevent humor from interrupting your timing, confidence, or conversational rhythm.""")
dodge_wind = AffinityPassiveSkills("Dodge Wind", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Wind (Curiosity / Connection) pulls. 
Thoughtful questions, rapport-building prompts, and conversational flow are recognized early, allowing you to pause or redirect before your attention, focus, direction, or disclosures are subtly guided.""")
dodge_psy = AffinityPassiveSkills("Dodge Psy", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Psy (Mind Reading / Psychological Perception) pressure. 
Psychological reads, pattern recognition, and insight-based observations are noticed early, allowing you to slow the interaction before those reads can be leveraged.""")
dodge_nuke = AffinityPassiveSkills("Dodge Nuke", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Nuke (Hype Building / Shared Energy) surges.
Collective enthusiasm, mirrored excitement, and momentum are recognized early, allowing you to delay engagement before energy can rush decisions or actions.""")
dodge_bless = AffinityPassiveSkills("Dodge Bless", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Bless (Kindness / Warmth) influence. 
Encouragement, positivity, and sincere goodwill are recognized early, allowing you to pause and reflect before warmth subtly shapes expectations, emotions, or choices.""")
dodge_curse = AffinityPassiveSkills("Dodge Curse", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Curse (Unconventional Moves / Unorthodoxy) pressure. 
Bold truth drops, self-deprecating remarks, risky or uncomfortable moves, and sudden frame shifts are recognized early, allowing you to pause, ground yourself, or redirect before discomfort or disruption can knock you off balance.""")
dodge_reverse_phys = AffinityPassiveSkills("Dodge Reverse Phys", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Phys (Aggression / Intimidation) pressure. 
Ego-driven dominance, raised voices, and coercive energy are recognized early, allowing you to pause, reframe, or slow the exchange before intimidation can create fear, submission, or escalation.""")
dodge_reverse_gun = AffinityPassiveSkills("Dodge Reverse Gun", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Gun (Nosiness / Prying) attempts. 
Intrusive questions and boundary-testing probes are noticed early, allowing you to delay, redirect, or respond non-committally before any leverage is gained.""")
dodge_reverse_fire = AffinityPassiveSkills("Dodge Reverse Fire", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Fire (Seduction / Validation) pressure. 
Performative charm, flattery traps, and attention bait are recognized early, allowing you to cool the interaction before ego pull, attraction bias, or obligation can form.""")
dodge_reverse_ice = AffinityPassiveSkills("Dodge Reverse Ice", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Ice (Hyperemotionality / Emotional Disregulation) pressure. 
Emotional flooding, guilt spirals, and volatile displays are noticed early, allowing you to slow, ground, or redirect before overwhelming or caretaking pressure sets in.""")
dodge_reverse_elec = AffinityPassiveSkills("Dodge Reverse Elec", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Elec (Mockery / Ridicule) attempts. 
Mean-spirited humor, sarcastic digs, and public jabs are recognized early, allowing you to disengage or slow the moment before embarrassment or provocation can land.""")
dodge_reverse_wind = AffinityPassiveSkills("Dodge Reverse Wind", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Wind (Conversational Steering / Feigned Interest) pressure. 
Leading questions and performative listening are detected early, allowing you to pause or redirect before your attention or conclusions are subtly guided.""")
dodge_reverse_psy = AffinityPassiveSkills("Dodge Reverse Psy", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Psy (Psychological Manipulation / Emotional Exploitation) pressure. 
Frame hijacks, guilt framing, and covert psychological tactics are noticed early, allowing you to slow the interaction before perception or decisions can be distorted.""")
dodge_reverse_nuke = AffinityPassiveSkills("Dodge Reverse Nuke", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Nuke (Impulsivity / Overstimulation) pressure. 
Chaotic hype, urgency, and emotional overload are recognized early, allowing you to slow pacing before overwhelm or impulsive action is triggered.""")
dodge_reverse_bless = AffinityPassiveSkills("Dodge Reverse Bless", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Bless (Ingenuine Kindness / Sincerity Facade) pressure. 
Performative warmth and fake positivity are recognized early, allowing you to pause before obligation, guilt, or trust shifts can form.""")
dodge_reverse_curse = AffinityPassiveSkills("Dodge Reverse Curse", "Affinity Passive", "N/A",
"""   - Increases your ability to sidestep Reverse Curse (Behavioral Corruption / Doubt Leverage) pressure. 
Subtle discouragement and hesitation-seeding are recognized early, allowing you to pause and reaffirm direction before doubt can slow action.""")

# Evade skills 
evade_phys = AffinityPassiveSkills("Evade Phys", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to move cleanly out of Phys (Bluntness / Assertiveness) pressure. Direct challenges, hard checks, and confrontational energy fail to land because you disengage, change positioning, or exit the exchange before force can be applied.""")
evade_gun = AffinityPassiveSkills("Evade Gun", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Gun (Low Risk / Light Probing) attempts entirely. Casual questions, value tests, and probes fail to connect because you shift topics, disengage, or remove access before probing can occur.""")
evade_fire = AffinityPassiveSkills("Evade Fire", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to bypass Fire (Charm / Charisma) influence. Flirting, teasing, and magnetic presence fail to land because you disengage emotionally or physically before attraction or sway can form.""")
evade_ice = AffinityPassiveSkills("Evade Ice", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Ice (Emotional Control / Emotional Maneuvering) attempts. Emotional pacing, validation, and composure-setting fail because you disengage before emotional guidance can begin.""")
evade_elec = AffinityPassiveSkills("Evade Elec", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Elec (Wit / Humor) disruption. Jokes, playful jabs, and timing-based pressure miss because you disengage before humor can affect rhythm or focus.""")
evade_wind = AffinityPassiveSkills("Evade Wind", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Wind (Curiosity / Connection) pulls. Questions, rapport-building, and conversational flow fail to connect because you disengage or change direction before connection can deepen.""")
evade_psy = AffinityPassiveSkills("Evade Psy", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Psy (Mind Reading / Psychological Perception) attempts. Psychological reads and insight-based pressure miss because you disengage before perception can be leveraged.""")
evade_nuke = AffinityPassiveSkills("Evade Nuke", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Nuke (Hype / Shared Energy) surges. Collective excitement and momentum fail to sweep you in because you step out before energy synchronization can occur.""")
evade_bless = AffinityPassiveSkills("Evade Bless", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Bless (Kindness / Warmth) influence. Encouragement and warmth fail to affect you because you disengage before emotional bonding or expectation forms.""")
evade_curse = AffinityPassiveSkills("Evade Curse", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Curse (Unconventional Moves / Unorthodoxy) pressure. Hard truths, discomfort, and risky frame shifts, power plays, and unorthodox moves fail to land because you disengage before disruption can occur.""")
evade_reverse_phys = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to move cleanly out of Reverse Phys (Aggression / Intimidation) pressure. Ego-driven dominance, coercive energy, raised voices, and attempts to force compliance fail to land because you disengage, reposition, or remove access before intimidation can apply pressure.""")
evade_reverse_gun = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Gun (Nosiness / Prying) attempts entirely. Intrusive questions, boundary-violating curiosity, and information-fishing fail because you disengage or change context before probing can occur.""")
evade_reverse_fire = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to bypass Reverse Fire (Seduction / Validation) pressure. Seductive charm, flattery traps, dramatized warmth, and attention-seeking behavior fail to land because you disengage before ego hooks, attraction bias, or obligation can form.""")
evade_reverse_ice = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Ice (Hyperemotionality / Emotional Disregulation) pressure. Emotional flooding, guilt spirals, volatile outbursts, and chaotic emotional displays miss entirely because you exit before emotional instability can spread or pull you in.""")
evade_reverse_elec = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Elec (Mockery / Ridicule) attacks. Mean-spirited jokes, sarcastic digs, and public jabs fail to land because you disengage before reaction windows open or social pressure can build.""")
evade_reverse_wind = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Wind (Conversational Steering / Feigned Interest) pressure. Leading questions, performative listening, and subtle conversational control attempts fail because you disengage before attention or direction can be guided.""")
evade_reverse_psy = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Psy (Psychological Manipulation / Emotional Exploitation) attacks. Gaslighting, guilt framing, frame hijacks, and covert psychological tactics miss because you disengage before perception, emotion, or decision-making can be distorted.""")
evade_reverse_nuke = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Nuke (Impulsivity / Overstimulation) pressure. Chaotic hype, emotional overload, urgency spirals, and reckless momentum fail to affect you because you disengage before overstimulation can take hold.""") 
evade_reverse_bless = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Bless (Ingenuine Kindness / Sincerity Facade) pressure. Performative warmth, fake positivity, and friendliness used for leverage fail because you disengage before trust, obligation, or emotional attachment can form.""")
evade_reverse_curse = AffinityPassiveSkills("Evade Reverse ", "Affinity Passive", "N/A",
"""   - Greatly increases your ability to avoid Reverse Curse (Behavioral Corruption / Doubt Leverage) pressure. Discouragement, hesitation seeding, and indirect fear-based influence fail because you disengage before doubt can slow momentum or corrupt action.""")

# Reists skills 
resist_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Phys (Bluntness/Assertiveness) attacks. Direct challenges, hard checks, and confrontational energy still register, but their pressure is significantly weakened. You remain composed, grounded, and in control when faced with blunt statements or dominance tests.""")
resist_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Gun (Low Risk / Light Probing) attacks. Casual questions, value tests, and surface-level information probes still register, but they extract little leverage or influence. You remain relaxed, selective, and in control of what you reveal during low-risk probing.""")
resist_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Fire (Charm / Charisma) attacks. Teasing, flirting, confident compliments, and magnetic presence still register, but their ability to sway your emotions or decisions is significantly weakened. You remain grounded, discerning, and self-directed in the presence of charm.""")
resist_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Ice (Emotional Control / Emotional Maneuvering) attacks. Emotional validation, mirroring, and temperature-setting still register, but their ability to steer your emotions, maneuver emotionally, or pace your decisions is significantly weakened. You remain composed and emotionally self-directed in regulated or emotionally charged situations.""")
resist_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Elec (Wit / Humor) attacks. Clever jokes, sharp wordplay, sarcasm, and playful jabs still register, but their ability to throw off your timing, confidence, or composure is significantly weakened. You stay mentally steady even when humor is used to disrupt or test you.""")
resist_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Wind (Curiosity / Connection) attacks. Thoughtful questions, rapport-building prompts, and conversational flow still register, but their ability to steer your focus, pace, or disclosures is significantly weakened. You remain anchored in your intent while engaging openly.""")
resist_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Psy (Mind Reading / Psychological Perception) attacks. Psychological reads, pattern calls, and subtle insight-based pressure still register, but their ability to influence your thoughts, emotions, or decisions is significantly weakened. You retain clarity and autonomy even when someone accurately reads you.""")
resist_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Nuke (Hype Building / Shared Energy) attacks. High-energy enthusiasm, raving, and momentum surges still register, but their ability to sweep you into decisions, commitments, or emotional highs is significantly weakened. You stay grounded and intentional even in highly charged group energy.""")
resist_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Bless (Kindness/Warmth) attacks. Genuine encouragement, positivity, and sincere goodwill are felt and appreciated, but they do not catch you off guard or influence your decisions. You remain steady, self-directed, and emotionally grounded even in the presence of warmth.""")
resist_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Curse (Unconventional Moves / Unorthodoxy) attacks. Self-deprecation, bold truth drops, risky or uncomfortable moves, and power-shifting actions still register, but they do not destabilize your confidence or sense of direction. You remain grounded when faced with discomfort or unconventional pressure.""")
resist_reverse_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Phys (Aggression / Intimidation) attacks. Ego-driven dominance, coercive pressure, and hostile confrontation still register, but their ability to intimidate, rush, or force compliance is significantly weakened. You maintain composure, posture, and autonomy under aggressive social pressure. """)
resist_reverse_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Gun (Nosiness / Prying) attacks. Intrusive questions, boundary-testing curiosity, and information-gathering attempts still occur, but they yield little usable leverage. You remain aware, guarded, and in control of what you reveal.""")
resist_reverse_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Fire (Seduction / Validation) attacks. Attention-seeking charm, flattery traps, and ego-driven warmth still register, but they fail to hook your emotions or steer your behavior. You remain grounded, discerning, and unaffected by performative allure.""")
resist_reverse_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Ice (Hyperemotionality / Emotional Disregulation) attacks. Emotional flooding, guilt spirals, and volatile outbursts still register, but their ability to destabilize or overwhelm you is significantly weakened. You remain steady, clear-headed, and emotionally regulated under pressure.""")
resist_reverse_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Elec (Mockery / Ridicule) attacks. Mean-spirited humor, sarcastic digs, and attempts to belittle or embarrass still register, but their ability to provoke, shame, or destabilize you is significantly weakened. You keep your composure and social footing when humor is used as a weapon.""")
resist_reverse_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Wind (Conversational Steering / Feigned Interest) attacks. Leading questions, performative listening, and subtle attempts to control the flow of conversation still occur, but they fail to redirect your thoughts, attention, or decisions. You remain mentally anchored and self-directed despite conversational manipulation.""")
resist_reverse_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Psy (Psychological Manipulation / Emotional Exploitation) attacks. Gaslighting, guilt framing, social proof pressure, and frame hijacks still register, but their ability to distort your perception or force compliance is significantly weakened. You retain clarity, autonomy, and independent judgment under manipulative pressure.""")
resist_reverse_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Nuke (Impulsivity / Overstimulation) attacks. Drama spirals, reckless hype, and chaotic emotional surges still occur, but their ability to overwhelm, rush, or exhaust you is significantly weakened. You maintain focus, pacing, and self-control amid excessive energy.""")
resist_reverse_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Bless (Ingenuine Kindness / Sincerity Facade) attacks. Performative warmth, back-handed compliments, toxic positivity, and friendliness used for leverage still register, but their ability to guilt, obligate, or manipulate you is significantly weakened. You remain discerning and self-directed in the presence of surface-level kindness.""")
resist_reverse_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Reduces the impact of Reverse Curse (Behavioral Corruption / Doubt Leverage) attacks. Veiled warnings, discouraging truth-drops, and insinuations meant to sow hesitation or fear still register, but their ability to stall your action or erode confidence is significantly weakened. You remain decisive and forward-moving despite attempts to inject doubt.""")

# Null skills 
null_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Phys (Bluntness / Assertiveness) attacks. 
Direct challenges, hard checks, and confrontational energy register as information only and produce no emotional or behavioral effect. 
Your composure, posture, and decision-making remain unchanged under blunt pressure.""")
null_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Gun (Low Risk / Light Probing) attacks. 
Casual questions, value tests, and surface-level info probes register as harmless noise and extract no leverage, insight, or influence. 
Your disclosures and direction remain unchanged.""")
null_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Fire (Charm / Charisma) attacks. 
Teasing, flirting, confident compliments, and magnetic presence are perceived without triggering emotional sway, attraction bias, or decision influence. 
Charm is recognized, but it produces no internal shift.""")
null_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Ice (Emotional Control / Emotional Maneuvering) attacks. 
Emotional validation, mirroring, composure-setting, and emotional maneuvering register only as neutral information and produce no emotional or behavioral effect. 
Your internal state, pace, and decisions remain fully self-regulated and unmoved.""")
null_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Elec (Wit / Humor) attacks. 
Clever humor, wordplay, playful jabs, and energetic wit are perceived clearly but cause no disruption to your timing, focus, or composure. 
Humor registers as neutral stimulation without knocking you off rhythm.
""")
null_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Wind (Curiosity / Connection) attacks. 
Thoughtful questions, rapport-building prompts, and conversational flow are perceived without redirecting your attention, pace, or disclosures. Curiosity registers as neutral interest and produces no influence.""")
null_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Psy (Mind Reading / Psychological Perception) attacks. 
Accurate reads, pattern recognition, and psychological insight are perceived as neutral information and produce no influence over your thoughts, emotions, or decisions. Being “read” does not grant leverage.""")
null_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Nuke (Hype Building / Shared Energy) attacks. 
Collective enthusiasm, mirrored excitement, and momentum surges are perceived without amplifying your emotions, urgency, or decisions. Shared energy registers as neutral stimulation and produces no pull.""")
null_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Bless (Kindness / Warmth). Encouragement, positivity, and sincere goodwill are received as neutral emotional signals and produce no internal shift, obligation, or influence. Warmth is acknowledged without affecting judgment, boundaries, or direction.""")
null_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Curse (Unconventional Moves / Unorthodoxy) attacks. 
Hard truths, self-deprecation, bold truth drops, and unorthodox or uncomfortable moves are perceived as neutral information and produce no destabilization. Unorthodox actions do not knock you off balance, and hard truths do not shake your confidence or sense of direction.""")
null_reverse_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Phys (Aggression / Intimidation) attacks. 
Ego-driven dominance, coercive pressure, raised voices, and attempts to force compliance register as noise and produce no fear, submission, or emotional reaction. Aggression has zero influence over your posture, decisions, or sense of control.""")
null_reverse_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Gun (Nosiness / Prying) attacks. Intrusive questions, boundary-violating curiosity, and information-fishing attempts register as harmless noise and extract zero usable intel or leverage. Your privacy, direction, and comfort remain unchanged.""")
null_reverse_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Fire (Seduction / Validation) attacks. 
Attention-seeking charm, flattery traps, dramatized warmth, and validation bait register as surface-level signals and produce no emotional pull, ego inflation, or behavioral influence. Performative charm has zero effect.""")
null_reverse_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Ice (Hyperemotionality / Emotional Disregulation) attacks. 
Emotional flooding, guilt spirals, volatile outbursts, and unregulated emotional pressure register as background noise and produce no emotional pull, overwhelm, or destabilization. Emotional chaos has zero effect on your internal state.""")
null_reverse_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Elec (Mockery / Ridicule) attacks. 
Mean-spirited jokes, sarcastic digs, public jabs, and attempts to belittle or embarrass register as empty noise and produce no shame, anger, or loss of composure. Ridicule has zero psychological effect.""")
null_reverse_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Wind (Conversational Steering / Feigned Interest) attacks. 
Leading questions, performative listening, and subtle attempts to guide your thoughts or control the flow of conversation register as empty structure and produce no redirection, influence, or attention capture. Your mental compass remains entirely self-directed.""")
null_reverse_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Psy (Psychological Manipulation / Emotional Exploitation) attacks. 
Gaslighting, guilt framing, frame hijacks, and covert psychological pressure register as transparent tactics and produce no distortion, compliance, or emotional reaction. Manipulation has zero effect.""")
null_reverse_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Nuke (Impulsivity / Overstimulation) attacks. 
Drama spirals, reckless hype, chaotic urgency, and emotional overload register as background noise and produce no rush, stress, or loss of control. Overstimulation has zero effect on your focus or pacing.""")
null_reverse_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Bless (Ingenuine Kindness / Sincerity Facade) attacks. 
Performative warmth, fake positivity, back-handed compliments, and friendliness used for image or leverage register as hollow signals and produce no emotional pull, obligation, or trust shift. Insincere kindness has zero effect.""")
null_reverse_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Completely nullifies Reverse Curse (Behavioral Corruption / Doubt Leverage) attacks. 
Subtle discouragement, veiled warnings, hesitation seeding, and indirect fear-based influence are recognized as tactics and produce no doubt, delay, or self-second-guessing. Attempts to sabotage action fail entirely.""")

# Drain
drain_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Phys (Bluntness / Assertiveness) pressure into clarity about power dynamics and intent. Direct challenges and confrontational energy connect, but instead of pressuring you, they give you intel on where the other party stands and what they are testing. Restores HP upon hit.""")
drain_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Gun (Low Risk / Light Probing) attempts into insight about how people use low-commitment questions and exploratory moves. Casual probes connect, but instead of drawing information from you, they reveal common probing patterns, pacing, and escalation logic behind low-risk social testing. Restores HP upon hit.""")
drain_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Fire (Charm / Charisma) influence into insight about attraction, persuasion, and social leverage. Charm connects, but instead of swaying you, it gives you intel on how and why they use charisma. Restores HP upon hit.""")
drain_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Ice (Emotional Control / Emotional Maneuvering) into understanding of emotional tactics. Validation and emotional pacing connect, but instead of guiding you, they give you intel on how emotions are being managed or directed. Restores HP upon hit.""")
drain_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Elec (Wit / Humor) disruption into actionable insight about timing, social rhythm, and reaction triggers. Jokes, wordplay, and playful jabs connect, but instead of throwing off your flow, they give you intel on how surprise, pacing, and humor are being used to create openings. Restores HP upon hit.""")
drain_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Wind (Curiosity / Connection) pulls into clarity about relational direction. Questions and rapport connect, but instead of steering you, they give you intel on where the conversation is meant to go and what genuine connection looks like. Restores HP upon hit.
""")
drain_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Psy (Mind Reading / Psychological Perception) into insight about perception patterns. Psychological reads connect, but instead of creating leverage, it gives you intel on how the other person analyzes and interprets behavior. Restores HP upon hit.""")
drain_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Nuke (Hype / Shared Energy) surges into insight about momentum creation. Collective excitement connects, but instead of rushing you, it gives you intel on how energy is being amplified. Restores HP upon hit.""")
drain_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Bless (Kindness / Warmth) into understanding of emotional bonding. Warmth connects, but instead of creating dependence, it gives you intel how trust and reassurance are being offered. Restores HP upon hit.""")
drain_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Curse (Unconventional Moves / Unorthodoxy) into insight about disruption and truth delivery. Discomfort connects, but instead of destabilizing you, it reveals where pressure creates growth or resistance. Restores HP upon hit.""")
drain_reverse_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Phys (Aggression / Intimidation) into insight about coercive dominance tactics. Aggressive pressure connects, but instead of provoking fear or submission, it reveals how intimidation is structured, timed, and escalated. Restores HP upon hit.""")
drain_reverse_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Gun (Nosiness / Prying) into insight about invasive probing mechanics. Intrusive questions connect, but instead of exposing you, they reveal how prying is disguised, sequenced, and used to gather leverage. Restores HP upon hit.""")
drain_reverse_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Fire (Seduction / Validation) into insight about validation traps and attention-seeking strategies. Performative charm connects, but instead of pulling you in, it reveals how flattery and allure are used to extract approval or control attention. Restores HP upon hit.""")
drain_reverse_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Ice (Hyperemotionality / Emotional Disregulation) into insight about emotional pressure tactics. Emotional flooding connects, but instead of overwhelming you, it reveals how guilt, volatility, and emotional excess are used to destabilize others. Restores HP upon hit.""")
drain_reverse_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Elec (Mockery / Ridicule) into insight about provocation and reaction-fishing. Ridicule connects, but instead of triggering emotion, it reveals how timing and embarrassment are used to bait reactions or lower status. Restores HP upon hit.""")
drain_reverse_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Wind (Conversational Steering / Feigned Interest) into insight about covert conversational control. Steering attempts connect, but instead of guiding you, they reveal how questions and attention shifts are used to subtly dominate direction.""")
drain_reverse_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Psy (Psychological Manipulation / Emotional Exploitation) into deep insight about manipulation frameworks. Psychological pressure connects, but instead of distorting you, it reveals how influence chains and leverage points are constructed.""")
drain_reverse_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Nuke (Impulsivity / Overstimulation) into insight about chaos-based pressure. Overstimulation connects, but instead of overwhelming you, it reveals how noise, urgency, and emotional overload are used to rush decisions.""")
drain_reverse_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Bless (Ingenuine Kindness / Sincerity Facade) into insight about image-based influence. Fake warmth connects, but instead of softening you, it reveals how friendliness and positivity are used to manufacture trust or obligation.""")
drain_reverse_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Allows you to convert Reverse Curse (Behavioral Corruption / Doubt Leverage) into insight about discouragement and hesitation seeding. Doubt-based pressure connects, but instead of slowing you, it reveals how fear and uncertainty are used to sabotage action.""")

# Repel
repel_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Phys (Bluntness / Assertiveness) overreach to backfire. Excessive directness, hard checks, or confrontational pressure overshoot the situation, making the attacker appear rigid, insecure, or socially miscalibrated. Causes the attacker to take damage. """)
repel_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Gun (Low Risk / Light Probing) misuse to backfire. Repeated or poorly timed probing makes the attacker seem unsure, unconfident, or directionless, reducing their perceived value. Causes the attacker to take damage. """)
repel_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Fire (Charm / Charisma) overuse to backfire. Excessive flirting, teasing, or performative charm feels forced or insincere, lowering attraction and credibility. Causes the attacker to take damage. """)
repel_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Ice (Emotional Control / Emotional Maneuvering) overreach to backfire. Attempts to regulate, validate, or manage emotions without invitation make the attacker appear controlling or emotionally detached. Causes the attacker to take damage. """)
repel_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Elec (Wit / Humor) overreach to backfire on the attacker. Poorly timed jokes, excessive cleverness, or forced wit overshoot the moment, breaking conversational rhythm and making the attacker appear socially miscalibrated or unserious. Causes the attacker to take damage.""")
repel_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Wind (Curiosity / Connection) overextension to backfire. Excessive questioning, forced rapport, or unnatural conversational flow becomes noticeable, making the attacker seem unfocused, intrusive, or agenda-driven. Causes the attacker to take damage. """)
repel_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Psy (Mind Reading / Psychological Perception) overreach to backfire. Premature interpretations, overconfident reads, or unearned psychological insight exposes faulty assumptions and reduces the attacker’s credibility. Causes the attacker to take damage. """)
repel_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Nuke (Hype / Shared Energy) excess to backfire. Forced excitement, overhyped momentum, or unregulated energy overwhelms rather than uplifts, draining the group instead of energizing it. Causes the attacker to take damage. """)
repel_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Bless (Kindness / Warmth) overuse to backfire. Excessive reassurance, unsolicited positivity, or emotional smoothing without context feels patronizing or hollow, eroding trust instead of building it. Causes the attacker to take damage. """)
repel_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Curse (Unconventional Moves / Unorthodoxy) misuse to backfire. Risky truth drops, discomfort plays, or abrupt frame shifts overshoot readiness, making the attacker appear reckless, unstable, or misaligned. Causes the attacker to take damage. """)
repel_reverse_phys = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Phys (Aggression / Intimidation) to backfire on the attacker. Ego-driven dominance, coercive pressure, or intimidation overshoots the situation, exposing insecurity and triggering social resistance rather than compliance.""")
repel_reverse_gun = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Gun (Nosiness / Prying) to backfire. Intrusive questioning, boundary violations, or information fishing becomes obvious, making the attacker appear invasive, creepy, or untrustworthy.""")
repel_reverse_fire = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Fire (Seduction / Validation) to backfire. Seductive charm, flattery traps, or attention-seeking behavior overshoots, reading as desperation or ego hunger instead of allure.""")
repel_reverse_ice = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Ice (Hyperemotionality / Emotional Disregulation) to backfire. Emotional flooding, guilt spirals, or volatile displays overwhelm the space, alienating others instead of drawing support.""")
repel_reverse_elec = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Elec (Mockery / Ridicule) to backfire. Mean-spirited jokes, sarcastic digs, or public ridicule overshoot, making the attacker look cruel, insecure, or socially unstable.""")
repel_reverse_wind = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Wind (Conversational Steering / Feigned Interest) to backfire. Leading questions, agenda pushing, or fake curiosity becomes noticeable, collapsing trust and control.""")
repel_reverse_psy = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Psy (Psychological Manipulation / Emotional Exploitation) to backfire. Gaslighting, guilt framing, or covert manipulation overreaches, revealing intent and destroying credibility.""")
repel_reverse_nuke = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Nuke (Impulsivity / Overstimulation) to backfire. Chaotic hype, urgency spirals, or emotional overload overwhelms others, isolating the attacker instead of rallying energy.""")
repel_reverse_bless = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Bless (Ingenuine Kindness / Sincerity Facade) to backfire. Performative warmth, fake concern, or toxic positivity slips, exposing insincerity eroding trust, and uncovering facades.""")
repel_reverse_curse = AffinityPassiveSkills("X", "Affinity Passive", "N/A",
"""   - Causes Reverse Curse (Behavioral Corruption / Doubt Leverage) to backfire. Subtle discouragement, hesitation seeding, or fear-based influence fails and instead hardens resolve, isolating the saboteur.""")
 
# Tuple that holds all Affinity Passive skills  
affinity_passive_skills = (dodge_gun, dodge_fire, dodge_ice, dodge_wind, dodge_psy, dodge_nuke, dodge_bless, dodge_curse, dodge_reverse_phys, dodge_reverse_gun, dodge_reverse_fire, dodge_reverse_ice,
dodge_reverse_elec, dodge_reverse_wind, dodge_reverse_psy, dodge_reverse_nuke, dodge_reverse_bless, dodge_reverse_curse)

# Passive Skills
diamond_mirror = PassiveSkills("Diamond Mirror", "Passive", "N/A",
"""   - Assume a composed, unyielding stance that mirrors the next incoming Physical-type attack (Phys and Gun attacks). You reflect the attack back at the target by mirroring the type of move they just used. 
If they throw a Physical attack, you throw one back. If they throw a Gun attack, you throw one back.
Ex: Them: "Where are you from" You: "Where are YOU from?" (Gun)
Ex 2: Them: "Go do that" You: "No, you go do that" (Phys)
Ex 3: Them: "Why should we hire you?" You: "What problem are you trying to solve right now?" (Gun)
Ex 4: Them: "Explain yourself" You: "Explain what outcome you're looking for" (Phys)
Ex 5: "Where do you live?" You: "What made you curious?" (Gun)""")


aegis_mirror = PassiveSkills("Aegis Mirror", "Passive", "N/A",
"""   - Assume a calm, refractive stance that mirrors the next incoming magical attack. When struck, the move is reflected back using the same element and intent, returning pressure without escalation. 
You reflect the attack back at the target by mirroring the type of move they just used. If they throw a Fire attack, you throw one back. If they throw an Ice attack, you throw one back, etc.
Ex: Them: "What got you into martial arts?" You: "What got you into the stuff you're passionate about?" (Wind)
Ex 2: Them: "You're pretty cute" You: "You're not bad looking yourself" (Fire)
Ex 3: Them: “Hey, you seem really genuine. I appreciate that” You: "I appreciate that you said that—thank you" (Bless)""")

regenerate_I = PassiveSkills("Regenerate I", "Passive", "N/A",
"""   - Gradually restores a small amount of HP over time when the user is in their natural recovery context. 
For extrovert-leaning users, HP regenerates during back-to-back social interactions where engagement fuels social stamina. 
For introvert-leaning users, HP regenerates during downtime, solitude, or disengaged states, where withdrawal and quiet restore stamina. Regeneration only occurs while the correct context is maintained; outside of it, no recovery is applied.
Ex: An extrovert chatting casually with coworkers between tasks feels more energized instead of drained.
Ex 2: An introvert taking a quiet break alone after a meeting feels their social stamina slowly return.""")

regenerate_II = PassiveSkills("Regenerate II", "Passive", "N/A",
"""   - Gradually restores a moderate amount of HP over time when the user is in their natural recovery context. 
Recovery is more noticeable and consistent, allowing sustained presence or faster rebound when pacing is respected. For extroverts, this manifests as continued energy during prolonged but balanced interaction. 
For introverts, this manifests as efficient recovery during solitude or disengagement periods.
Ex: An extrovert remains steady during a long but relaxed group conversation.
Ex 2: An introvert recovers most of their stamina during a longer solo break after a social obligation.""")

regenerate_III = PassiveSkills("Regenerate III", "Passive", "N/A",
"""   - Gradually restores a large amount of HP over time when the user is in their natural recovery context. 
Enables high endurance and long-term stability, provided the user consistently plays to their temperament. Regeneration remains inactive if the user stays in a mismatched context for too long.
Ex: An extrovert can stay socially active for extended periods without burning out, as long as interactions stay healthy and balanced.
Ex 2: An introvert can fully reset after withdrawing into solitude, returning refreshed and composed.""")
invigorate_I = PassiveSkills("Invigorate I", "Passive", "N/A",
"""   - Gradually restores a small amount of SP over time when the user is in their natural mental recovery context. 
For extrovert-leaning users, SP regenerates during active engagement that feels mentally stimulating, such as discussion, collaboration, or light problem-solving with others.""")

invigorate_II = PassiveSkills("Invigorate II", "Passive", "N/A",
"""   - Gradually restores a moderate amount of SP over time when the user is in their natural mental recovery context. 
Mental recovery is more noticeable and reliable, allowing sustained Persona usage without immediate burnout. 
For extraverts, mental stamina is maintained through continued but balanced engagement. For introverts, focused solitude or low-stimulus environments rapidly restore mental energy. 
Ex: An extravert stays mentally engaged across long collaborative conversations without fogging out.
Ex 2: An introvert regains most of their mental energy after uninterrupted focus time.  """)

invigorate_III = PassiveSkills("Invigorate III", "Passive", "N/A",
"""   - Gradually restores a large amount of SP over time when the user is in their natural mental recovery context. 
Enables high mental uptime and frequent Persona skill usage, provided the user consistently respects their recovery condition. Remaining in the wrong context suppresses recovery entirely. 
Ex: An extravert thrives mentally during long, engaging exchanges without losing sharpness.
Ex 2: An introvert fully resets their mental energy after extended uninterrupted solitude.""")

gun_boost =  PassiveSkills("Boost", "Passive", "N/A",
"""   -  Increases the effectiveness and consistency of Gun (Low Risk / Light Probing) skills. 
Your questions and light probes are better timed, better framed, and more likely to land cleanly, extracting clearer signals without escalating risk. 
Reduces misfires and increases the chance of creating openings (1 Mores). 
Probes feel natural, not forced, you get better read on interest and alignment, and you have higher success rates on low-risk tests.""")

fire_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Fire (Charm / Charisma) skills. 
Your teasing, flirting, confident compliments, and charismatic delivery are better timed and better calibrated, landing smoothly without feeling forced or excessive. 
Charm is applied with control, increasing attraction and engagement while reducing misfires. 
Charm feels natural, not try-hard, flirting lands without awkwardness, and charismatic moves generate interest more reliably. """)

ice_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Ice (Emotional Control / Emotional Maneuvering) skills. 
Your validation, mirroring, de-escalation, and emotional pacing are better timed and better calibrated, allowing you to stabilize situations and guide emotional tone without overreaching. 
Emotional regulation lands smoothly, de-escalation works more reliably, and mirroring doesn’t feel manipulative or forced.""")

elec_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Elec (Wit / Humor) skills. 
Your jokes, wordplay, and playful jabs are better timed and cleaner in delivery, allowing humor to land without disrupting flow. Improves rhythmic control, reducing mistimed humor and increasing the chance to create brief staggers and openings. 
Humor lands cleanly instead of derailing the moment, witty remarks create micro-staggers (openings) and fewer awkward beats or forced jokes.""")

wind_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Wind (Curiosity / Connection) skills. 
Your questions, follow-ups, and expressions of interest are smoother and better timed, keeping conversational flow alive without forcing direction. Reduces dead ends and improves natural momentum. 
Increases the effectiveness and consistency of Wind (Curiosity / Connection) skills. Your questions, follow-ups, and expressions of interest are smoother and better timed, keeping conversational flow alive without forcing direction. 
Reduces dead ends and improves natural momentum. Follow-up questions feel natural, not interrogative, flow is maintained even on weak topics, fewer awkward pauses or forced pivots.""")

psy_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Psy (Mind Reading / Psychological Perception) skills. 
Your reads, pattern recognition, and psychological assessments are more accurate and better timed, reducing misreads and increasing confidence in when to act on gathered insight. 
Reads land more often and with less hesitation, fewer false assumptions or premature conclusions, Psy skills connect cleanly without overreaching.""")

nuke_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Nuke (Hype Building / Shared Energy) skills. 
Your enthusiasm, energy matching, and hype-building are better calibrated, allowing you to amplify group momentum without overshooting or destabilizing the interaction. 
Shared excitement feels natural, not forced, energy syncs instead of spiraling, group morale rises without chaos.""")

bless_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Bless (Kindness / Warmth) skills. 
Your encouragement, sincerity, and positive intent land cleanly without overgiving or blurring boundaries. 
Warmth feels grounded and respectful, building trust without obligation. Kindness feels genuine, not performative, encouragement uplifts without creating dependency, and trust builds steadily, not artificially.""")

curse_boost = PassiveSkills("Boost", "Passive", "N/A",
"""   - Increases the effectiveness and consistency of Curse (Unconventional Moves / Unorthodoxy) skills. 
Your bold statements, uncomfortable truths, and frame-breaking actions are better calibrated and better timed, allowing you to disrupt stagnation or surface authenticity without destabilizing yourself. 
Unorthodox moves land without social self-sabotage, hard truths are delivered with control, not recklessness, risk is intentional, not impulsive, fewer misfires when breaking convention.""")

gun_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly increases the power and precision of Gun (Low Risk / Light Probing) skills. 
Your probes are surgical and instinctively timed, rapidly extracting high-quality signals while maintaining minimal risk. 
Enables faster chains, clearer openings, and stronger follow-ups, often setting up 1 Mores or immediate escalations. 
Probes cut straight to signal, not noise, rapid calibration of interest, alignment, and momentum, light questions create heavy openings, and seamless transitions from probing to action.""")

fire_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies the power and authority of Fire (Charm / Charisma) skills. 
Your presence, teasing, flirting, and confident speech become instinctively calibrated and magnetic, shaping attraction, attention, and momentum with minimal effort. 
Charm no longer just lands—it sets the frame. 
Charisma pulls people toward you effortlessly, Flirting escalates naturally without chasing and Fire skills more easily trigger Weaknesses, 1 Mores, or All-Out Attacks.""")

ice_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery over Ice (Emotional Control / Emotional Maneuvering) skills. 
You instinctively regulate emotional climates, guide pacing, and maintain composure under pressure. 
Emotional maneuvers shape the interaction effortlessly, allowing you to neutralize volatility or establish calm authority. 
Emotional chaos stabilizes around you, tension dissolves without explanation, and you set the emotional pace of the room.""")

elec_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery of Elec (Wit / Humor) skills. 
Your timing becomes instinctive and surgical—humor doesn’t just land, it disrupts rhythm, creates clean staggers, and opens immediate follow-ups. 
Wit controls the pace of the interaction without turning mean or performative. 
Jokes consistently create openings (stagger / 1 More), you interrupt others’ momentum while keeping yours intact, humor guides tempo instead of stealing focus.""")

wind_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery of Wind (Curiosity / Connection) skills. 
You instinctively guide conversational currents, turning responses into momentum and cycling interactions toward stronger topics with minimal effort. 
Flow becomes directional—connection deepens or disengages cleanly. 
You steer conversations without obvious control, strong topics emerge naturally from weak ones, Wind skills more easily trigger Weaknesses, 1 Mores, or clean exits.""")

psy_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery of Psy (Mind Reading / Psychological Perception) skills. 
Psychological insight becomes instinctive and decisive—patterns, intentions, and emotional states are recognized rapidly and leveraged with precision. 
Psy no longer just observes; it dictates optimal action.  
Reads are fast, confident, and actionable, you capitalize immediately on hesitation or tells, and psychological pressure escalates without guesswork.""")

nuke_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery of Nuke (Hype Building / Shared Energy) skills. 
You instinctively synchronize energy across individuals or groups, creating contagious momentum that rallies others and sustains engagement. 
Hype becomes focused and directional, not explosive or erratic. 
Group energy locks into sync around you, momentum sustains instead of burning out, Nuke skills more easily trigger Weaknesses, 1 Mores, or group follow-ups.""")

bless_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery of Bless (Kindness / Warmth) skills. 
Your presence radiates calm goodwill and emotional safety, stabilizing interactions and strengthening trust effortlessly. 
Positivity becomes an anchor—others feel seen and steady around you without manipulation. 
Warmth disarms tension naturally, trust forms quickly but stays healthy, Bless skills more easily neutralize negativity or despair.""")

curse_amp = PassiveSkills("Amp", "Passive", "N/A",
"""   - Greatly amplifies mastery of Curse (Unconventional Moves / Unorthodoxy) skills. 
You wield risk and discomfort with instinctive precision, using bold, unconventional actions to break false frames and force authenticity without destabilizing yourself. 
Hard truths and rule-breaking moves no longer threaten your balance—they reframe the encounter. 
Unorthodox moves land cleanly and decisively, discomfort exposes truth instead of creating chaos, Curse skills more reliably trigger Weaknesses, collapses, or decisive momentum shifts.""")

# Tuple that holds all normal Passive skills 
passive_skills = (diamond_mirror, aegis_mirror, regenerate_I, regenerate_II, regenerate_III, invigorate_I, invigorate_II, invigorate_III, gun_boost, fire_boost, ice_boost, elec_boost, wind_boost, psy_boost, nuke_boost, bless_boost, curse_boost,
gun_amp, fire_amp, ice_amp, elec_amp, wind_amp, psy_amp, nuke_amp, bless_amp, curse_amp)
