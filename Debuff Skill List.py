# Filename: Debuff Skill List.py
# Date: 2/11/26
# Author: Aoi | shadowsnowwolf
# List of Debuff Skills 

class DebuffSkills:
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

class SingularSkills(DebuffSkills):
    pass

class AOESkills(DebuffSkills):
    pass

# AOE Debuff skills 
ether_break = SingularSkills("Ether Break", "Atk Debuff | Tarunda effect", 8,
"""   - Pierce the surface of a Shadow’s attack by identifying the root cause behind the blow — projection, venting, manipulation, displaced emotion, nervousness, hidden discomfort, or external events (e.g., a bad day, personal stress). 
By internally understanding the dynamic (e.g., ‘projection’, ‘fear response’, ‘ego trigger’, ‘social anxiety’, ‘cope’, ‘insecurity’, ‘emotional outburst’, etc.), you sever its emotional tether and reduce its impact on you. 
The Shadow’s attack power collapses because once you understand why they are acting this way, the blow no longer hits you with full force, causing their social leverage to lose effect. 
This realization creates a psychological barrier that disarms emotional energy — they can still swing, but the hits are weakened. 
Awareness breaks enchantment: once you see the why, the what can no longer wound you. 
It’s also about recognizing that the Shadow’s reactions stem from themselves, not you, which reduces your internal damage. 
On hit, the target’s attack is temporarily reduced. Can be stacked and reapplied.""")

ascendancy_link = SingularSkills("Ascendancy Link", "Def Debuff | Rakunda effect", 8,
"""   - Leverage social proof and preselection by subtly showcasing desirability, status, value through accomplishments, or prior approval from others. 
This might be done by revealing your socials to the target after gaining proof of value to others (i.e, a large follower account on Instagram, positive engagement/support from others on your social, engaging content that aligns with the target’s interests, etc). 
The display of credibility makes the target take you more seriously and drop their guard, perceiving you as someone of higher social standing rather than a random NPC. 
This perception shift drastically lowers their need to quality test you, reducing their social defenses. 
On hit, the target's defense is temporarily reduced. Can be stacked and reapplied.""")

tactic_diffuser = SingularSkills("Tactic DIffuser", "Ag Debuff | Sakunda effect", 8,
"""   - Engage your social instincts to perceive the tactic or maneuver behind a Shadow’s move, whether that be probing, baiting, manipulative questioning, scamming, shit testing, boundary testing, behavior manipulation, or attempts at information extraction. 
Unlike Ether Break, which exposes the why behind an attack, Tactic Diffuser focuses on the what: the actual strategy or maneuver they are attempting. 
By recognizing the tactic before it lands, you gain a brief internal window of awareness (“Ahhh, I know what they’re trying to hit me with”), giving you time to dodge their attack, counter, or neutralize its effect. 
Their swing still exists, but their precision falters. 
(Ex: Someone tries to manipulate you into doing what they want against your will and you recognize what they’re trying to do. Awareness of what they’re doing reduces the chances of it working on you.)
On hit, the target's accuracy/evasion is temporarily reduced. Can be stacked and reapplied.""")

affinity_beacon = SingularSkills("Affinity Beacon", "Atk + Def + Ag Debuff | Debilitate effect", 30,
"""   - Lean on familiarity, mutual connections, shared context, or prior recognition to subtly lower the target’s social guard. By referencing mutual connections, prior introductions, or common experiences, you create an approachable expectation from the target that encourages receptivity and trust. 
This internal and external resonance creates a window where your interactions land more smoothly, and your influence is felt more readily. 
The target’s attacks, defensive readiness, and precision are reduced because your presence carries credibility, familiarity, or trust. 
This skill thrives in interactions where social history or word-of-mouth familiarity exists. 
(Ex: Someone at a networking event has heard of your work through mutual acquaintances. Their social pressure or skepticism is reduced, making it easier to steer the conversation or establish rapport.
Ex 2: A group is initially hesitant or testing you, but a shared connection or prior interaction softens their defenses, lowering the effectiveness of their “tests.”
Ex 3: You get a reference from a friend for a job through connections, and the employers seem particularly fond of you due to your relationship with the accomplice). 
On hit the target’s attack, defense, and accuracy/evasion is temporarily reduced. Can be stacked and reapplied (as long as social familiarity persists).""")


# AOE Debuff skills 
frequency_barrier = AOESkills("Frequency Barrier", "AOE Atk Debuff | Matarukaja effect", 24,
"""   - Expand your awareness across the entire social field to perceive the hidden structure, frequency, and agenda driving any group. 
You pinpoint the core psychology binding them together, revealing the true motives at play whether it's status preservation, cult-like dynamics, toxic conformity, negativity contagion, ego contagion, image control, escapism, “fall-in-line” mentality, etc. —and sever its emotional hold on you the moment you see it. 
Once you recognize the blueprint, you detach effortlessly-- their approval or disapproval loses meaning and their coordinated energy collapses. 
Even in environments thick with social pressure or judgment, your composure remains unshaken as the realization forms an invisible barrier of understanding that dulls the emotional force behind group attacks which can include gossip, or manipulation attempts. 
By recognizing both positive and negative crowd agendas, you navigate social spaces with clarity and precision, able to engage strategically without absorption or confusion. 
You realize that the group's approval or disapproval of you has nothing to do with your worth but entirely about their own distortion of agendas. 
On hit, all Shadows in the group’s attack is temporarily reduced. Can be stacked and reapplied.""")

contagion_wave = AOESkills("Contagion Wave", "AOE Def Debuff | Marakukaja effect", 24,
"""   - Trigger a social ripple effect via strategic preselection and social proof. 
By earning visible approval or positive reactions from one or two influential members within a group, you set off a chain reaction of perception—others instinctively follow the lead of those already impressed. 
This indirect display of social proof reframes you from ‘outsider’ to ‘socially validated’, lowering the group’s collective guard. 
As your perceived value climbs, the need for others to test or challenge you diminishes, causing their defenses to drop in unison. 
Through exploiting tribalism, you’re able to get the approval of the group. 
On hit, all Shadows in the group’s defense is temporarily reduced. Can be stacked and reapplied.""")

coordination_vector = AOESkills("Coordination Vector", "AOE Ag Debuff | Masukukaja effect", 24,
"""   - Engage your social instincts to chart the tactical currents of a group, sensing the maneuvers, patterns, and strategies they attempt to execute — coordinated influence, pressure, social nudges, or orchestrated persuasion aimed at steering your choices. 
Unlike Frequency Barrier, which reduces the emotional weight of their motives, Coordination Vector targets the precision of their actions. 
By anticipating their moves, you create an internal window of insight that lets you sidestep, counter, or disrupt their coordinated swings. 
Their attacks still come, but the group’s accuracy falters, making it harder for their maneuvers to land as intended. 
Your awareness of their mechanics reduces the chance that their moves succeed as intended.
(Ex: A group tries to peer pressure you into doing drugs saying it's the 'socially acceptable' thing to do. Your awareness of the peer pressure reduces their accuracy.
Ex 2: A group tries to push their product onto you through validating each other’s opinions or claiming social conformity). 
On hit, all Shadows in the group’s accuracy/evasion is temporarily reduced. Can be stacked and reapplied.""")

singular_skills = (ether_break, ascendancy_link, tactic_diffuser, affinity_beacon)
aoe_skills = (frequency_barrier, contagion_wave, coordination_vector)
