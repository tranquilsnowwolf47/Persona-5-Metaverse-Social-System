# Filename: CurseSkillList.py
# Date: 2/10/26
# Author: Aoi | shadowsnowwolf
# List of Curse skills (Unconventional Moves/Unorthodoxy)

class CurseSkillls:
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


class SevereSkills(CurseSkillls):
    pass

class InstantKillSkills(CurseSkillls):
    pass

class HeavySkills(CurseSkillls):
    pass

class MediumSkills(CurseSkillls):
    pass

class LightSkills(CurseSkillls):
    pass

ex = HeavySkills("", "Curse", "Heavy", 0,
"""   - 
""")


# Severe Damage Grade Skills
honey_basher = SevereSkills("Honey Basher", "Curse", "Severe", 30,
"""   - A long-term Curse skill that weaponizes time and restraint.
Rather than committing to an exclusive relationship during the honeymoon phase during the talking/dating stage of a potential romantic interest—when novelty, dopamine, and idealization distort judgment, you intentionally delay full commitment from as little as 6 months to as long as several years. 
As the chemical high fades and comfort replaces effort, the target’s baseline behavior emerges, revealing their true behavior and your true compatibility. 
Deals severe Curse damage.""")


# Instant Kill Skills
black_list = InstantKillSkills("Black List", "Curse", "Instant kill", 25,
"""   - When flakey behavior crosses your preset tolerance window (as early as the first flake, never later than the third), the target is immediately cut off—DM closed, unfollowed, or access revoked. 
No message is sent and no clarification is offered. This move treats lack of follow-through as final intent, cutting through excuses and ambiguity by removing the target from your attention economy entirely. 
Designed to preserve momentum, enforce standards, speed-run options, and eliminate low-investment connections. 
Very high chance of inflicting instant kill.""")

effort_reaper = InstantKillSkills("Effort Reaper", "Curse", "Instant kill", 15,
"""   - Monitors the target’s communication over time, tracking patterns of short, non-committal, or disengaged responses. 
Once their minimal effort crosses your set threshold, you end the interaction entirely, removing them from your roster without ceremony. 
This decisive move eliminates “dry” time-wasters before they drain more of your energy or block better opportunities. 
Functions as an instant kill against low-effort communicators; misses entirely if the target maintains healthy engagement. 
High chance of inflicting instant kill.""")

timeout_clause = InstantKillSkills("Timeout Clause", "Curse", "Instant kill", 15,
"""   - When dealing with new connections, you set a strict 5-day window (or any other window of your choice) for replies. 
If they haven’t responded by the deadline, you close the conversation without further effort. 
This move filters out low-investment individuals, protects your time, and prevents you from chasing dead-end interactions. 
Works best when applied consistently to maintain strong boundaries. Against flaky or uninterested targets, it can function like a delayed instant kill. 
High chance of inflicting instant kill.""")

flake_snare = InstantKillSkills("Flake Snare", "Curse", "Instant kill", 7,
"""   - Call out the gap between someone's words and actions when they cancel or "can't make it" without offering a new time. 
By directly asking if they'd like to reschedule or pointing out the lack of follow-up, you force clarity on their intent. 
This move can flush out low investment, reveal disinterest, test for reactions, or motivate genuine people to lock in another time. 
Highly effective against those who habitually flake, but risks social tension if the excuse was genuine. 
Medium chance of inflicting instant kill.""")


# Heavy Damage Grade Skills
data_hex = HeavySkills("Data Hex", "Curse", "Heavy", 12,
"""   - Steer the conversation with carefully framed prompts and follow-ups to coax personal details and extract desired information from the target. 
By masking probing questions as genuine curiosity, you lower their guard and draw out insights they may not have intended to share. 
The information you harvest can then lead to 1 Mores, build rapport faster, create information leverage, or be used to qualify or disqualify someone based on how they choose to respond. 
If used carefully and mindfully, you can allow the target to reveal the desired information you want without them feeling like you’re interrogating them. 
This can lead to a technical to tailor other elemental follow-ups (Ex: Fire, Psy, Wind, Nuke) for maximum impact and can give you great intelligence for battle strategy.
Overuse or too-obvious questioning risks triggering the person's guard or becoming disengaged if they catch on and realize that they're revealing too much. 
Can be very effective for disqualifying low-value individuals or revealing key details like relationship history, coping mechanisms, lifestyle patterns, dependency, mental health status, personal values, etc. 
(Ex: “Do you have a lot of friends?”, 
Ex 2: “What’s the exact medication and dosage you need a refill for?”
Ex 3: “Do you know the name of your insurance company?”
Ex 4: “How would you describe your last ex?”
Ex 5: “Do you go to parties much?”
Ex: 6: “Who’s someone that you wish you were still close with?”). 
Deals heavy Curse damage.""")

hidden_blueprint = HeavySkills("", "Curse", "Heavy", 13,
"""   - Deliberately withhold details of long term goals, future plans, or upcoming moves, revealing nothing until you've already achieved or nearly achieved them. 
This secrecy creates a compelling aura of mystery and prevents others from gaining leverage over your ambitions, nullifying chances of sabotaging your progress in a long, delayed gratification journey. 
(Ex: Withholding your plans to talk about the job you applied for until after you get it. 
Prevents copers from criticizing your decision to get that specific job that you felt was best for you or getting a job in general
Ex 2: Not telling negative family members about your long term career goals until you've gotten significant results in the grand scheme of things). 
Deals heavy Curse damage.""")

veiled_initiative = HeavySkills("Veiled Initiative", "Curse", "Heavy", 11,
"""   - Intentionally refrain from sharing spontaneous, sensitive plans, early ambitions, or vulnerable details that would invite criticism, discouragement, or meddling. 
By withholding information that others could judge, sabotage, or talk you out of, you force your target’s Shadow to operate in the dark where uncertainty breeds hesitation. 
This skill is built on the foundation of human nature that people often undermine what they don’t understand. 
By keeping your moves hidden, you deny them the leverage of clarity, preventing their doubts or projections from becoming obstacles.
(Ex: You want to try a new cooking recipe, but if you tell your nagging family members, they'll tell you all about how you can't do it and that you shouldn't try. 
By not telling the and just doing it, you nullify their negative opinion before it comes, protecting the trajectory of your progress).
Deals heavy Curse damage.""")


# Medium Damage Grade Skills
friendzone_seal = MediumSkills("Friendzone Seal", "Curse", "Medium", 9,
"""   - Preemptively establish a strictly platonic frame before romantic feelings or expectations can develop. 
By casually positioning the connection as “friends only” early on, you prevent romantic interpretation at the root and keep the dynamic clean, comfortable, and aligned. 
This skill quietly closes a romantic route before it ever opens, avoiding future awkwardness or emotional buildup.
(Ex: “You’re honestly a really good friend”
 Ex 2: “I’m glad we’re friends—I like the vibe”
 Ex 3: “You’re like a sister to me”
 Ex 4: “You’re someone I’d totally grab food with as a friend”
 Ex 5: “You remind me of my friends back home”).
Deals medium Curse damage.""")

dark_tease = MediumSkills("Dark Tease", "Curse", "Medium", 7,
"""   - Deliver a playful jab at the target's quirks or habits. 
Your teasing is enough to amuse confident types and gain points for playful types, but can backfire on the insecure and sensitive. 
When it lands successfully, it sparks banter and promotes playful conversation.
(Ex: "Seriously, you only know how to cook one recipe? Some chef you are"
Ex 2: “You’re that ripped and you don’t even work out? You’ve got to be kidding”
Ex 3: "People are supposed to laugh when you make a joke you know").
Deals medium Curse damage.""")

blackout = MediumSkills("Blackout", "Curse", "Medium", 8,
"""   - Purposely withhold response to the target's words or provocations, letting silence and ambiguity do the work. 
By ignoring them, you refuse to engage– defusing their eagerness for conflict, creating a mystery spark that piques their curiosity, as well as disables problematic behavior, shifting the power dynamic in your favor. 
Particularly effective against people who are eager to start arguments, conflict, or problems. 
Deals medium Curse damage.""")

verbal_hex = MediumSkills("Verbal Hex", "Curse", "Medium", 7,
"""   - Boldly challenge the target's opinion, inviting tension, debate, or deeper engagement. Can gain you respect or trigger someone's ego depending on how it's used. 
A risky but rewarding move if used in the right scenario. 
Hitting them with a "Why do you think that?" or a “You sure about that?” is a great way of achieving this effect-- however, it can bruise egos and trigger someone to let their guard up or shut the conversation down entirely if used on the wrong temperament. 
Deals medium Curse damage.""")

chrono_veil = MediumSkills("Chrono Veil", "Curse", "Medium", 7,
"""   - Intentionally delay making plans or responding to requests, creating anticipation, mystery, and a sense of value around your time. 
This creates a scarcity effect which amplifies the target's curiosity and investment, while also preserving your emotional bandwidth and reinforcing healthy boundaries. 
Delay committing time to the target for a chosen interval of time to build excitement, stimulate emotions, and make the time that you spend with them more fulfilling. 
Deals medium Curse damage.""")

refusal_rite = MediumSkills("Refusal Rite", "Curse", "Medium", 7,
"""   - Deny the target's request, whether it's time, a favor, attention, or energy. 
This assertion of boundaries commands respect, asserts authority, and can reveal the true nature of the connection. 
Extremely effective for testing the authenticity of the connections and to see how the other person reacts. 
This skill can be fantastic at revealing someone's priorities, level of self-security, and see if someone is trying to use you for favors or resources. 
(Ex: Person: “Can you get my groceries for me?” You: ”Nope”). 
Deals medium Curse damage.""")

minimum_echo = MediumSkills("Minimum Echo", "Curse", "Medium", 9,
"""   - Respond to inquiries with only enough detail to acknowledge the question. 
By disclosing only minor or vague details, you can create mystery and compel the target to dig deeper or reveal more. 
This controlled withholding lowers their informational defense, sparks curiosity, and can unsettle those who prefer certainty or direct answers. 
Giving minimal details also assists in maintaining firm boundaries from those who seek to extract information about you that they could use against you, establish power dynamics over you, or keep the information in mind for malicious gain. 
By giving away almost nothing, you deny others the ammo they'd need to bait or manipulate you. 
(Ex: Them: “Where exactly do you live?” You: “South side.” (short pause, change topic), 
Ex 2: Them: “What’s your salary range?” You: “Enough to cover the important stuff” (smile, move the conversation elsewhere) 
Ex 3: Them: What kind of car did you come in? You: “An SUV”). 
Deals medium Curse damage. """)

catalyst_trigger = MediumSkills("Catalyst Trigger", "Curse", "Medium", 7,
"""   - Say a daring statement or challenge that cuts past small talk and presses on sensitive territory, challenging the other person in some way. 
This assertive risk can spark spirited debate or deeper honesty, but if mistimed, it can trigger the Shadow's guard or disengage them. 
Use this skill to jolt the interaction off autopilot and force genuine reactions.
(Ex:"I bet you're only here to impress people, aren't you?"
Ex 2: “You seem to talk a lot about helping others but it doesn’t seem like you’re really doing it”). 
Deals medium Curse damage.""")

clock_hold = MediumSkills("Clock Hold", "Curse", "Medium", 7,
"""   - After securing someone’s contact information, you intentionally wait an extended period before re-initiating contact. 
This calculated pause disrupts expectations, subtly signaling independence and high value while fostering anticipation and curiosity. 
On invested targets, it can heighten intrigue and make your eventual message land with greater impact. 
On low-investment or easily distracted targets, it risks cooling their interest entirely. 
Best used when you’ve already left a strong first impression. 
Deals medium Curse damage.""")

reality_spike = MediumSkills("Reality Spike", "Curse", "Medium", 4,
"""   - Drop a blunt, unfiltered observation that shatters the flow of polite conversation, exposing an unspoken truth or tension the target would rather keep hidden. 
This direct strike can destabilize their composure, strip away facades, and force genuine reactions. 
Powerful for breaking through false fronts, but risks backlash and triggering egos if used recklessly. 
(Ex: “You can keep lying to be about this, but you can’t lie to yourself forever.”, 
Ex 2: “How long are you gonna keep deluding yourself on this?”
Ex 3: “It’s pretty obvious that these people don’t actually care about you at all”
Ex 4: “You’re not stuck. You’re just too scared to pick the harder path.”
Ex 5: “You keep saying that you want better, but you’re clinging to the exact habits that are holding you down”
Ex 6: “If you really cared you would have done something by now.”
Ex 7: “You keep blaming circumstances, but deep down you know it’s your lack of commitment”
Ex 8: “Come on. You already know why you’re unhappy. You just don’t want to admit it”). 
Deals medium Curse damage.""")

hollow_stance = MediumSkills("Hollow Stance", "Curse", "Medium", 6,
"""   - Emit an emotionally detached aura of indifference. 
By showing little visible investment in the target and displaying little care in their words, and their actions, you introduce ambiguity that can spark curiosity, frustrate needy behavior, or shift the power balance in your favor. 
Showing neutrality may trigger certain emotional effects in the target which could be effective for maintaining boundaries and testing the target's resilience. 
Deals medium Curse damage.""")


# Light Damage Grade Skills
mocking_mirror = LightSkills("Mocking Mirror", "Curse", "Light", 4,
"""   - Crack a light joke at your own expense. 
This intentional self-depreciation can show humility and humanize yourself which can disarm the target, lower their defenses, and spark empathy or playful teasing. 
Overuse or overly harsh self-put-downs risks undermining your frame, inviting loss of respect or disengagement from the target if they start to see you as low-value. 
Strategic use of this skill is advised.
(Ex: "I'm the worst cook you've ever met", 
Ex 2: "Don't mind my dance moves, I dance like a drunk dodo bird"
Ex 3: "Don’t bring me near devices. I break everything I touch"). 
Deals light Curse damage.""")

cursed_joke = LightSkills("Cursed Joke", "Curse", "Light", 5,
"""   - Unleash a sharply-edged dark humor joke that lands best with those who appreciate an edgier and darker sense of humor. 
On a willing audience, it sparks laughter and a sense of shared mischief. 
If used on the wrong Shadow type however, it can be resisted entirely, and may trigger discomfort, mental barriers, or create the ick if used on the wrong personality type. 
This high-risk move can forge rapid rapport with the right crowd or backfire miserably if mistimed. 
Deals light Curse damage.""")

vanity_bait = LightSkills("Vanity Bait", "Curse", "Light", 5,
"""   - Deliver a compliment with little to no genuine sentiment, crafted to bait ego-driven targets into revealing their vanity or self-importance. 
On narcissistic or approval-hungry individuals, this can prompt them to drop their guard, overshare, or chase further validation. 
Against perceptive or self-secure targets, however, the move can backfire—damaging rapport or making you appear insincere. 
Best used sparingly and with a clear follow-up plan to exploit the information gained. 
Deals light Curse damage and has a chance of lowering the target’s Defense.""")

faux_focus = LightSkills("Faux Focus", "Curse", "Light", 4,
"""   - Feign attentiveness, listening to keep the target’s ego satisfied while conserving your own mental energy. 
Through well-timed nods, vague affirmations, and occasional eye contact, you create the illusion of engagement without genuinely processing their every word. 
Especially effective against narcissists or distorted individuals who punish perceived inattention during long, self-indulgent rants. 
Overuse risks dulling genuine rapport with healthy people, but against the wrong crowd, it can save you from unnecessary conflict or drama. 
Deals light Curse damage.""")

severe_skills = (honey_basher)
instant_kill_skills = (black_list, effort_reaper, timeout_clause, flake_snare)
heavy_skills = (data_hex, hidden_blueprint, veiled_initiative)
medium_skills = (friendzone_seal, dark_tease, blackout, verbal_hex, chrono_veil, refusal_rite, minimum_echo, catalyst_trigger, clock_hold, reality_spike, hollow_stance)
light_skills = (mocking_mirror, cursed_joke, vanity_bait, faux_focus)
full_curse_skill_list = (severe_skills, heavy_skills, medium_skills, light_skills)
