# Filename: Ice Skill List.py
# Date: 2/7/26
# Author: Aoi | shadowsnowwolf
# List of Ice skills (Emotional control/manuvering)

class IceSkills:
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

class SevereSkills(IceSkills):
    pass

class HeavySkills(IceSkills):
    pass

class MediumSkills(IceSkills):
    pass

class LightSkills(IceSkills):
    pass

example = MediumSkills("X", "Ice", "Medium", 0,
"""   - X""")

thermal_reset = HeavySkills("Thermal Reset", "Ice", "Heavy", 14,
"""   - You intentionally disengage from a tense or emotionally volatile situation, suspending reaction, speech, and decision-making until composure is fully restored. This halts impulsive behavior, prevents regret-based actions, and reasserts emotional sovereignty. You refuse to act while compromised. Useful in high-stake arguments, authority conflicts, relationship flashpoints, or texts you really want to clap back to. Deals heavy Ice damage and may cure Rage, Fear, and Confusion for the user. 
""")

crystal_resonsance = HeavySkills("Crystal Resonance", "Ice", "Heavy", 12,
"""   - You recall something emotionally meaningful the person previously shared and reflect it with care. 
It shows you're not just listening but holding the information close to them.  
(Ex: "You said this kind of thing drains you. Want to step away?", 
Ex 2: "You talked about how much that mattered to you. I didn’t forget"
Ex 3: “Your name’s Samantha right? I know I forget sometimes but I made sure to not let this one slip”)
Ex 4: “Persona 5 is your comfort game yeah? You mentioned it really helped you get through some tough times in your life”)
Ex 5: “You said your brother taught you that move. It makes sense why it stuck with you”
Ex 6: “It’s clear to see that the reason why you’re so determined is because of the family member you lost”.) 
Deals heavy Ice damage.""")

platonic_curtain = MediumSkills("Platonic Curtain", "Medium", "Heavy", 8,
"""   - Lower the emotional temperature and clearly establish platonic intent when friendliness is misinterpreted as flirtation or when romantic boundaries already exist. 
Through calm tone, neutral framing, and emotional maturity, you remove ambiguity without embarrassment, rejection, or tension. 
This stabilizes the interaction, preserves mutual respect, and prevents future misunderstandings or social fallout.
(Ex: “Oh, I’m just being friendly—I like good conversations.”
 Ex 2: “Nothing like that, I keep things pretty platonic.”
 Ex 3: “I’m not flirting, don’t worry—I’m just relaxed.”
 Ex 4: “I’m very clear when I’m interested; this is just friendly.”
 Ex 5: “Especially when someone’s taken, I keep things respectful.”
 Ex 6: Calm delivery, relaxed posture, no apology).
Deals medium Ice damage.""")

glacier_wall = MediumSkills("Glacier Wall", "Ice", "Medium", 8,
"""   - A calm statement that gently enforces your boundaries without escalating the situation. 
Used when someone pushes past comfort, tries to test limits, or asks a question that makes you uncomfortable regardless if their intention is malicious or not. 
(Ex: "I don’t really want to talk about that" 
Ex 2: “It’s complicated"
Ex 3: “It’s not something I really talk about often”). 
Deals medium Ice damage.""")

cold_admission = MediumSkills("Cold Admission", "Ice", "Medium", 10,
"""   - Calmly and directly acknowledge your mistake without excuses, emotional leakage, or self-deprecation. 
By taking clean accountability, you immediately lower emotional temperature, halt escalation, and stabilize the interaction. 
This prevents defensive spirals, disarms hostility, and reasserts composure through emotional maturity. 
(Ex: "Yeah, that was my fault"
Ex 2: "I misread that. That one's on me"
Ex 3: "You're right-- I dropped the ball there"
Ex 4: "I should have paid better attention. I won't let that happen next time").
Deals medium Ice damage.""")

safe_space = MediumSkills("Safe Space", "Ice", "Medium", 8,
"""   - You lower your emotional armor intentionally, making space for the other person to open up. Creates trust through subtle vulnerability and grounded energy. 
(Ex: "You don't have to talk about it if you're not ready, just know I'm not judging" , 
Ex 2: "We can talk about it whenever is most comfortable for you. You can take your time."
Ex 3: ”I get what you’re going through. Just know that you don’t have to deal with it alone. I’m always a contact away”
Ex 4: “You don’t have to explain anything you don’t want to.”
Ex 5: “If it helps, we can just sit for a bit or go for a walk. No rush”
Ex 6: “Whatever pace feels right for you is fine with me”
Ex 7: “I’m here to listen if you ever need to talk.”). 
Deals medium Ice damage.""")

anchor_presence = MediumSkills("Anchor Presence", "Ice", "Medium", 9,
"""   - Radiate a calm, collected aura that steadies the atmosphere with your presence. 
By staying grounded and listening without interrupting, you give space for others to vent or speak while your presence naturally cools tension. 
Whether someone’s spiraling, overreacting, or running hot, your stillness grounds the room, helping them regulate by syncing with your vibe. 
Not reacting to emotional energy diffuses the energy on its own, and you remain still and steady while someone vents or talks without interrupting. 
Ex: A customer is upset with you, but you don’t react and remain calm and professional, their anger and tension starts to diffuse on their own seeing as they didn’t get you to react. 
Deals medium Ice damage.""")

soulshare = MediumSkills("Soulshare", "Ice", "Medium", 8,
"""   - You share a personal story, experience, or moment that reveals something real about yourself that allows you to relate on an emotional level with your target. 
It's meant to connect and relate rather than impress. Soulshare creates emotional resonance, helping others feel seen, safe, or inspired. 
The story doesn't need to be dramatic, it just needs to be genuine and delivered with self-awareness and intention. 
(Ex: Sharing a time you overcame fear in a relatable way 
Ex 2: Telling an embarrassing story when someone feel embarrassed about something they did to help them feel less stupid 
Ex 3: Sharing about an awkward, funny moment when someone deals with rejection 
Ex 4: Revealing a past failure and how you overcame it to give someone inspiration when they’ve dealt with failure
Ex 5: Sharing a memory that mirrors someone else's experience to build rapport, 
Ex 6: Sharing about an experience you had when someone goes through a similar difficulty to relate the feeling). 
Deals medium Ice damage.""")

cooldown = MediumSkills("Cooldown", "Ice", "Medium", 9,
"""   - Gently but firmly reduce emotional tension in a heated or uncomfortable situation. 
Whether someone is getting loud, defensive, or passive-aggressive, Cooldown slows the momentum without grounding energy, which restores clarity and safety to the conversation. 
Rather than overpowering, it regulates the vibe through maturity and composure. 
(Ex: "Let's take a breath, I'm not here to argue", 
Ex 2: "I can tell this matters to you. I want to understand, not fight” 
Ex 3: “I think we’re both a little on edge. Let’s reset, yeah?”, 
Ex 4: "I’m not trying to escalate. Let’s slow this down"). 
Deals medium Ice damage.""")

frostfade = MediumSkills("Frostfade", "Ice", "Medium", 8,
"""   - Calmly disengage or redirect from a social situation that drains, discomforts, or disrespects you. Whether through an excuse, a gentle shutdown, or a smooth redirection, Frostfade allows you to exit gracefully without emotional friction. 
It prioritizes emotional safety, control, and self-respect, and helps you preserve energy when staying would cost you too much. Also good to use when you feel low chemistry between the parties. 
(Great for female Phantom Thieves for dealing with creepy dudes).
(Ex: "Hey, I'm gonna bounce for now, not really feeling this energy", 
Ex 2: "I actually have to check on something. I'll catch you later", 
Ex 3: "You know, I don't think this is my vibe. Take care though", 
Ex 4: "Sorry, I just saw someone I need to say hi to", 
Ex 5: “Sorry, I have somewhere to be”
Ex 6: “It was nice meeting you but I’ve gotta head out now”). 
Deals medium Ice damage.""")

icebreak_shield = MediumSkills("Icebreaker Shield", "Ice", "Medium", 7,
"""   -  During conflicts or heated discussions, you express your perspective using “I statements” to reduce perceived aggression. 
Your calm, measured delivery defuses tension, keeps the conversation controlled, and makes the other person more receptive to your point of view. 
(Ex: “I feel frustrated when plans change last minute. It makes it hard for me to stay organized.”
Ex 2: “I feel overwhelmed when there’s a lot happening at once, can we slow down?”
Ex 3: “I notice I get tense when this topic comes up, so I wanted to share my perspective calmly”
Ex 4: “I feel like we might be misunderstanding each other, let me clarify my side”
Ex 5: “I feel ignored when I’m sharing something important and I don’t feel heard”
Ex 5: “I feel pressured when decisions are made for me instead of with me”).
Deals medium Ice damage.""")

reflective_icebreak = MediumSkills("Reflective Icebreaker", "Ice", "Medium", 7,
"""   - Once rapport has been established, you create a pause in the flow to reflect on something meaningful that was said, not to analyze, but to show you've been listening, feeling, and absorbing the moment. 
This move deepens connection through thoughtful recognition, emotional mirroring, or subtle vulnerability, gently cooling any remaining tension beneath the surface. 
(Ex: "It's cool hearing how passionate you are about that, it really shows", 
Ex 2: "Honestly, I didn't expect this convo to get real, but I'm glad it did.", 
Ex 3: "I can relate. Not the same situation, but that feeling? I get it." , 
Ex 4: "You've got more depth than I expected when we first started talking"
Ex 5: “I’m glad we were able to have a conversation like this. I really felt a click in our viewpoints”
Ex 6: “That part of the conversation gave me a clearer picture of where you’re coming from”). 
Deals medium Ice damage.""")

emotional_mirror = MediumSkills("Emotional Mirror", "Ice", "Medium", 7,
"""   - Go deeper by validating not just the emotion, but its importance to them. 
Shows you recognize the meaning behind what they feel, building comfort and trust.
(Ex: “You were in a relationship with them for years. I could imagine the heartbreak of losing them”
Ex 2: "Your relationship with your wife is sacred to you, I can see that."
Ex 3: “Learning a martial art ended up being that important to you because it helped you learn self respect. That’s powerful."
Ex 4: “I see why this trinket means so much to you. The memories you carried in it”
Ex 5: “I know how much this dojo means to you. It’s like your happy place”). 
Deals medium Ice damage.""")

mirrored_empathy = MediumSkills("Mirrored Empathy", "Ice", "Medium", 6,
"""   - Empathize with the target in a way that show’s relation to their feelings to stabilize negative feelings through validation. 
Effective when someone is venting or openly emotional, showing you’re on the same wavelength. 
(Ex: "I totally get why you're upset. That would bother me too" 
Ex 2: “I’d be pretty upset too if that happened. You’re not alone in feeling that way”
Ex 3: "That sounds overwhelming. I’d feel the same way in your shoes"
Ex 4: “You’re not overreacting. Anyone would feel that way after dealing with that”
Ex 5: “You deserve to rest after that. It sounds exhausting”).
Deals medium Ice damage.""")

reasurring_chill = LightSkills("Reassuring Chill", "Ice", "Light", 4,
"""   - Gently reassure someone who feels uneasy or anxious by providing calm and steady emotional support. 
Ideal when sensing anxiety, nervousness, or hesitation in someone. 
Saying something along the lines of: "It's okay, take your time" can ease tension in conversation and help the target relax. 
Deals light Ice damage.""")

acknowledgement_frost = LightSkills("Acknowledgement Frost", "Ice", "Light", 3,
"""   - Briefly and clearly acknowledge another's viewpoint, signaling genuine understanding without extensive emotional commitment. 
When you acknowledge the person, you do so without emotional weight. 
Useful for minor frustrations, casual concerns, or when you want to acknowledge without overinvesting. 
Effective when someone shares a minor frustration or a casual concern. 
(Ex: "Yeah, I get that. I see where you’re coming from"
Ex 2: “I can see why you think that now”
Ex 3: “Your perspective makes a lot of sense when you put it like that.”
Ex 4: “I didn’t view it that way before, but it makes a lot of sense now.”
Ex 5: “I get the logic behind that. It checks out”
Ex 6: “Given all the facts, I can understand how you arrived at that”). 
Deals light Ice damage.""") 
