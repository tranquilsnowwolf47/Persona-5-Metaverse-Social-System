# Filename: Fire Skill List.py
# Date: 2/6/26
# Author: Aoi | shadowsnowwolf
# List of Phys (Charm/Charisma) skills from the Metaverse Social System sorted by damage grade 

class FireSkills:
    def __init__(self,name, element, damage_grade, SP_cost, description):
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

class SevereSkills(FireSkills):
    pass

class HeavySkills(FireSkills):
    pass

class MediumSkills(FireSkills):
    pass 

class LightSkills(FireSkills):
    pass

example = quick_probe = HeavySkills("Quick Probe", "Gun", "Heavy", "",
"""   - X""")

value_touch = HeavySkills("Value Touch","Fire","Heavy", 11,
    """   - Use a silver tongue and refined framing to subtly persuade the target on how they perceive value, more commonly when it comes to products and services. Rather than explaining or selling, you weave benefits into the conversation so the offer feels obvious, sensible, and personally relevant. Your tone is confident, warm, and assured, making the deal feel less like a transaction and more like a smart, natural choice. Resistance lowers as the target becomes more willing to see upside, convenience, and long-term gain.
(Ex 1: “A lot of people don’t realize this, but our membership plans usually cut costs significantly—especially for families.”
Ex 2: “Most people don’t notice it at first, but plans like this usually end up saving a lot more than they cost.”
 Ex 3: “It’s one of those things that doesn’t sound big until you realize how often people actually use it.”
 Ex 4: “For families especially, it tends to simplify everything instead of nickel-and-diming each visit.”
 Ex 5: “It’s not about spending more—it’s about avoiding the stuff that quietly adds up.”
 Ex 6: “That’s usually why people who try it don’t go back.”
 Ex 7: “For insurance and cash-pay patients, it ends up being way more flexible and usually saves people hundreds over time.”
 Ex 8: “It’s especially helpful if you come in more than once a year—it kind of pays for itself.”
 Ex 9: “Most families like it because everyone’s covered instead of juggling separate visits.”
 Ex 10: “It’s not something everyone needs, but for people who use care regularly, it makes things way simpler.”
Ex 11: “If you want, I can explain how it works real quick.”
Ex 12: “How about we take a look at these pretty knives? We have some pretty good limited time deals right now”)
Ex 13: “Oh it definitely saves a lot. You could be saving hundreds per year and never have to pay copays and balances while getting an infinite number of visits on your time”
Ex 14: “If you get the premium membership it’ll end up costing you less over time than if you kept renewing the previous membership for months on top of you getting more benefits”).
Deals heavy Fire damage.""")

heat_check = MediumSkills("Heat Check", "Fire", "Medium", 9,
"""   - A playful yet deliberate flirtation that sparks attraction without overcommitting. Heat Check applies heat through confident implication rather than overt pursuit— teasing interest, planting curiosity, and seeing if the spark is returned. It’s lighthearted on the surface, but purposeful underneath, making it ideal for testing romantic interest while maintaining composure and control.
(Ex 1: “Is this your plan to make me more curious or is it just me?
Ex 2: “Is that your way of getting my attention?”
Ex 3: “You always talk like that or am I special today?”
Ex 4: “You say that like you don’t know what you’re doing”
Ex 5: “You’re not as subtle as you think”
Ex 6: “You’re playing a dangerous game”).
Deals medium Fire damage.""")

flame_tease = MediumSkills("Flame Tease", "Fire", "Medium", 6,
"""   - Deliver a playful, confident remark that lightly challenges or teases the target, sparking chemistry and engagement without being mean-spirited. 
Perfect for building tension, flirtation, or playful rapport in a bold and forward way while keeping your presence magnetic.
(Ex: "Ohhh, so you’re that kind of trouble."
Ex 2: "You’ve clearly got people figured out. I’ll need to stay on my toes around you then.”
Ex 3: “Mysterious type. Better keep my eye on you then. 
Ex 4: “Is this your strategy or are you just naturally this unpredictable?”
Ex 5: “So this is how you get attention huh?”
Ex 6: “Trying to mess with me on purpose?”).
Deals medium Fire damage.""")

confidence_burn = MediumSkills("Confidence Burn", "Fire", "Medium", 7,
"""   - Radiate self-assurance naturally– confidence that glows naturally, not to impress anyone. 
You speak with quiet certainty, displaying that your value is self-generated, internally gratified, unshakable, and non-performance-based. 
Your presence commands respect and social impact without trying or performing.  
(Ex: "I know I’m not for everyone. That’s kind of the point"
Ex 2: "I always choose being respected over being liked. I’m not afraid to be hated if it means staying true to myself"
Ex 3: “I already know I’m handsome and charming. No need to prove it”
Ex 4: “I don’t have time to hang out with just anyone. I prioritize being with the strong”
Ex 5: “I don’t drop my standards. I know my worth)
Ex 6: “I don’t really care if they don’t want to be friends with me. I never fall in line).
Deals medium Fire damage.""")

magnetic_presence = MediumSkills("Magnetic Presence", "Fire", "Medium", 9,
"""   - Command attention and radiate confidence and magnetism nonverbally just through superior posture, tone, eye contact, etc. 
It’s charm through energy, presence, and vibe, not words. The way you carry yourself projects quiet confidence, increasing your social impact. 
(Ex: While standing, stand up straight without slouching
Ex 2: While walking, walk your back straight, shoulders back, and your chest out
Ex 3:  Speak naturally with appropriate intonation relaxation that displays confidence). 
Deals medium Fire damage.""")

value_burn = MediumSkills("Value Burn", "Fire", "Medium", 8,
"""   - Acknowledge the target’s skill, uniqueness, talents, or subtle qualities in a way that makes them feel seen, valued, and appreciated. 
Delivered with confident charm, it sparks respect and admiration, creating a subtle social pull. Ideal for reinforcing their value while maintaining your charismatic presence. 
(Ex: “I didn’t expect someone to handle that so smoothly. Consider me impressed.”
Ex 2: “Not everyone could pull that off like the way you just did” 
Ex 3: “I’m surprised to have met someone as skilled as you”
Ex 4: “You’re a natural when it comes to this finance stuff. I could learn a lot from you” 
Ex 5: “That spinning hook kick was crazy. You must be a pro at your art”
Ex 6: “You’ve got a sharp mind. This makes this conversation way more interesting”).
Deals medium Fire damage.""")

ember_gaze = MediumSkills("Ember Gaze", "Fire", "Medium", 7,
"""   - Maintain strong, steady eye contact with the target. 
Your gaze radiates confidence, subtle charm, and self-security. 
Avoiding eye contact signals submission, nervousness, and insecurity; this skill flips the dynamic, giving you a commanding, magnetic presence. 
By showing that you’re not afraid to look away, you signal confidence, charm, and dominance through non-verbal communication. 
Deals medium Fire damage.""")

inferno_grip = MediumSkills("Inferno Grip", "Fire", "Medium", 6,
"""   - Extend a firm, confident handshake that radiates grounded charm and charisma. 
The physical contact and nonverbal communication leaves a strong impression, subconsciously earning you respect from others and drawing the other person into your presence. 
Deals medium Fire damage.""")

lady_shake = MediumSkills("Lady Shake", "Fire", "Medium", 6,
"""   - Execute a calibrated masculine handshake designed specifically for greeting women, accounting for the fact that many women naturally offer a lighter, more relaxed grip. 
You match their hand size and pressure while maintaining firm structure, ensuring the shake feels confident and grounded—never soft, never overpowering. 
This creates a balanced first impression that communicates to the woman strength, social intelligence, confidence, and respect without discomfort or awkwardness. Deals medium Fire damage.""")

velvet_note = MediumSkills("Velvet Note", "Fire", "Medium", 7,
"""   - Drop a spontaneous voice note into the target’s DMs, breaking the rhythm of your usual conversation. 
Its unpredictability generates excitement and makes it stand out, drawing attention and leaving the recipient intrigued, smiling, or eager to respond. 
Most effective when texting is the norm and voice notes are unexpected. Deals medium Fire damage. """)

high_lighter = LightSkills("High Lighter", "Fire", "Light", 5,
"""   - Shine a warm, confident spotlight on the fact that the target chose to be here with you. Whether they came to an event, grabbed food, or just showed up for the moment, your acknowledgment lands as charismatic appreciation — not neediness. It can deepen rapport, lower emotional defenses, and triggers a 1 More by making the shared experience feel more intentional and meaningful. Best used once the interaction already has some rhythm and energy to it.
(Ex: "I appreciate you coming out with me– makes this thing way better”
Ex 2: "Glad you pulled up with me. You make events a lot more fun"
Ex 3: “I appreciate you being here with me today– solid choice”
Ex 4: “I appreciate you being here with me. Makes the moment hit different” 
Ex 5:  “You could've been anywhere else today. I like that you chose to be here”). 
Deals light Fire damage.""")

confident_compliment = LightSkills("Confident Compliment", "Fire", "Light", 5,
"""   - A bold, unapologetic compliment delivered with relaxed confidence — acknowledging their attractiveness without pedestalizing them or losing frame. It’s shameless in the sense that you don’t hide your interest, but smooth enough to avoid any creepiness. The charisma comes from owning the compliment, not chasing approval. This skill warms the interaction, sparks attraction, and shows you’re unafraid to speak truth with swagger.
(Ex: "Yeah, you look good in that. I’m sure you already knew it though." 
Ex 2: "Those nails are doing you some real justice."
Ex 3: “You look really good today. Figured I should say it before anyone else does.
Ex 4: “Okay, that look’s doing you some favors”
Ex 5: “You’re seriously owning that look”).
Deals light Fire damage. """)

vocal_flare = LightSkills("Vocal Flare", "Fire", "Light", 4,
"""   - A subtle but intentional use of vocal emphasis—slight pitch variation, warmth, and expressive stress on key words—to make your speech feel engaging, charming, and confident. Rather than slowing the conversation, Vocal Spark adds color and magnetism to your delivery, making ordinary lines feel intentional and attractive. It’s not about being louder or deeper—it’s about where you place the emphasis. 
(Ex: (in tone) "You noticed that, didn't you?" ,
Ex 2: "I like how you think." ,
Ex 3: "Oh, is that so?"). 
Deals light Fire damage. """)

gentlemans_flattery = LightSkills("", "Fire", "Light", 4,
"""   - A confident, well-placed compliment that highlights a specific, standout detail about the target—how they think, present themselves, or carry effort. Rather than generic praise, this skill signals attentiveness and taste. Delivered smoothly and without overexplaining, it feels bold and flattering, lowering defenses through charisma instead of overt kindness or validation. This move communicates: “I notice details—and I say what I notice.”
(Ex: "You explain things insanely well. The way you break it down actually makes sense"
Ex 2: “I’m loving your Attack on Titan shirt. You’ve got some great taste”
Ex 3: “That new haircut is fresh man. The fade is on point”
Ex 4: “Your smile is pretty contagious you know that?”
Ex 2: “I’m loving your fade bro. You look like a whole chad”
Ex 6: “Is that a Katana umbrella? That’s just sick”).
Deals light Fire damage.""")

charming_smile = LightSkills("Charming Smile", "Fire", "Light", 4,
"""   - Flash a confident, charming smile the moment you make eye contact. No words needed, your charisma does the talking nonverbally. 
This simple gesture carries a magnetic energy that can pull the target in, making you appear bold, attractive, and self-assured. 
Deals light Fire damage. """)



severe_skills = ()
heavy_skills = (value_touch)
medium_skills = (heat_check, flame_tease, confidence_burn, magnetic_presence, value_burn, ember_gaze, inferno_grip, lady_shake, velvet_note)
light_skills = (high_lighter, confident_compliment, vocal_flare, gentlemans_flattery, charming_smile)
