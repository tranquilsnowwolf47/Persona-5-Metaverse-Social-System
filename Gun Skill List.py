# Name: Gun Skill List.py
# Date: 2/6/26
# Author: Aoi | shadowsnowwolf
# List of Gun (Low risk/light probing) skills from the Metaverse Social System sorted by damage grade 

class GunSkills:
    def __init__(self, name, element, damage_grade, HP_cost, description): # Constructor
        self.name = name
        self.element = element
        self.damage_grade = damage_grade
        self.HP_cost = HP_cost
        self.description = description

    # Shows the full info of the skill
    def display_skill(self):
        print(f" - {self.name} ({self.element})")
        print(f"HP Cost: {self.HP_cost}")
        print(f"Description:\n{self.description}")

class SevereSkills(GunSkills):
    pass

class HeavySkills(GunSkills):
    pass

class MediumSkills(GunSkills):
    pass

class LightSkills(GunSkills):
    pass

# Template variable 
example = quick_probe = HeavySkills("Quick Probe", "Gun", "Heavy", "",
"""   - X""")

quick_probe = HeavySkills("Quick Probe", "Gun", "Heavy", "20%",
"""   - During a brief interaction, you ask 2–3 carefully chosen questions designed to read the target’s interest, energy, and reciprocation with surgical precision. 
The questions are casual but precise, giving you meaningful insight while keeping the interaction low-risk. 
Each question is casual on the surface, but strategically chosen to reveal how engaged they are, how they think, and whether they’re genuinely open to you, just being polite, or if they’re not interested at all. 
By compressing meaningful intel into moments, you can instantly decide whether to press the advantage, pivot, or disengage entirely. If the target gives dry, low-effort responses, their guard drops and a clean All-Out Attack becomes possible. 
If they shine back with intrigue or enthusiasm, you get a natural 1 More to deepen the connection. Ideal for cold approaches where you need to assess whether someone is worth pursuing further.
(Ex: “How do you usually spend your free time?”
Ex 2: “Who do you usually meet up with when you’re just chilling?”
Ex 3: “What’s been keeping you busy these days?”
Ex 4: “So how do you usually unwind after a long week?”
Ex 5: “Got any hobbies or side projects you’re really into?”
Ex 6: “Do you usually stick with a close crew, or meet new people often?”
Ex 7: “What are you studying if you don’t mind me asking?”).
Deals heavy Gun damage.""")

quick_invite = MediumSkills("Quick Invite", "Gun", "Medium", "15%",
"""   - Casually extend an invitation light enough to stay chill, but pointed enough to shift the dynamic. Quick Invite is the social equivalent of tossing the ball into their court without overplaying your hand. 
It’s a mid-risk, mid-reward move used to test interest and escalate the relationship if it’s meant to be. Best used after minor rapport has been established as timing and tone are needed to effectively use the skill. 
Advances interaction without pressure, but may lose power if overused or delivered with hesitation. 
(Ex: "I was thinking of checking out the vendor hall. Want to tag along?", 
Ex 2: "I’m getting food soon. You’re welcome to come with.", 
Ex 3: "You seem cool. Wanna link up later if we’re still around?"
Ex 4: “If you’re still gonna be around later, we should link up at the cosplay meet”
Ex 5: “I’m hopping over to the artist alley. Wanna come scout with me?”). 
Deals medium Gun damage.""")

sniper_question = MediumSkills("Sniper Question", "Gun", "Medium", "11%",
"""   - Take a specific detail that the target mentioned– a slip, a hint, or a breadcrumb, and fire it off like a test shot. 
This question cuts through vague conversation, forces the target to elaborate on a point they made earlier, lowers their evasiness, and pushes them into authenticity without risking major backlash if they dodge. 
(Ex: "You said you love surprises. Which one actually surprised you?"
Ex 2: “You mentioned that you travel a lot. What’s your best trip so far and how?
Ex 3: “You said you ‘kinda know how to cook’-- what’s your signature dish?
Ex 4: “You mentioned you like older games– what era are we talking?”
Ex 5: “You said you’re into fitness– what part of it keeps you hooked?”). 
Deals medium Gun damage.""")

interest_probe = MediumSkills("Interest Probe", "Gun", "Medium", "10%",
"""   - Fire off a subtle, target question to uncover potential shared interests, hobbies, or passions. 
This recon move lets you gauge compatibility, spark enthusiasm, and collect conversation fuel, all without overcommitting or seeming too invested. Best used early in a conversation after greetings or light remarks to test chemistry and detect engagement. 
If the target responds with engagement and reciprocity, it creates a 1 More opportunity, revealing their affinities and conversational strengths. 
Perfect for conventions, casual meetups, waiting in line, or when you see someone in an environment and want to start conversation. 
(Ex: "You into anime or just passing through?", 
Ex  2: (After spotting a cosplay): "Ever been to Megacon?", 
Ex 3: "You play games much?"
Ex 4: “Do you come to the gym often?
Ex 5: (Seeing someone hitting a punching bag): “So what’s your art background?” 
Ex 6: “Any hobbies that take up all your free time?”
Ex 7: “So what kind of coffee and entrees do you usually get here?”
Ex 8: “You know any good clothing shops?”).
Deals medium Gun damage. """)

weekend_needle = MediumSkills("Weekend Needle", "Gun", "Medium", "10%",
"""   - Ask a casual, timely question about the target’s upcoming or recent weekend to gauge their availability, lifestyle, or overall vibe. 
This low-pressure move allows you to gauge the target’s lifestyle without getting personal and opens the door to shared plans or deeper conversation without directly inviting them. 
If their reply comes back engaged or enthusiastic, you gain a clean 1 More opportunity. 
(Ex: “Got anything fun planned this weekend?”
Ex 2: “What did you get up to last weekend?”
Ex 3: “Are you having a chill weekend or a busy one?”
Ex 4: “Any cool plans lined up for the weekend?”).
Deals medium Gun damage. """)

soft_deflect = MediumSkills("Soft Deflect", "Gun", "Medium", "12%",
"""   - Fire a calm, precise verbal shot to redirect unwanted behavior, conversation, or boundary-crossing intentions without overcommitting. 
Soft Deflect acts as a low-risk, high-reward maneuver by asserting boundaries, preserving your frame, and reasserting your position without full-on aggression. 
Keeps you in high-value social standing by not overreacting. 
(Ex: "Sorry, I’m not really the drinking type.",
Ex 2: “That’s not my thing, but good luck with it.
Ex 3: “I usually pass on that kind of stuff respectfully”
Ex 4: "You might be barking up the wrong tree there",
Ex 5: "I'm not really interested in hearing about drama to be fair",  
Ex 6: “I’m not really into that stuff”
Ex 7: “I’m not really in the mood for that to be honest”).
Deals medium Gun damage.""")

social_probe = MediumSkills("Social Probe", "Gun", "Medium","12%",
"""   - Ask a swift, low commitment question at first to gauge a person's social availability/openness and interest in networking outside the moment. 
You ask the target if they have social media, and their response extracts their level of investment/receptiveness to further connection. High chance of triggering a Hold Up. If they say yes, you get the chance to trigger a Shadow Negotiation. 
If an excuse comes up, it gives you the opportunity to All-Out Attack.
(Ex: “Do you use Instagram/Snapchat?”
Ex 2: “Do you have Instagram/Snapchat by any chance?”
Ex 3: “Are you on Instagram/Snapchat?”
Ex 4: “Which apps do you usually use to stay in touch?”). 
Deals medium Gun damage.""")

subject_grenade = MediumSkills("Subject Grenade", "Gun", "Medium", "10%",
"""   - Subtly shift the subject to a topic more meaningful to both parties when in awkward or unideal situations. Subject Grenade is used when the current topic isn’t ideal, awkward, boring, irrelevant, or something you can’t contribute to. 
Instead of trying to force the moment, this low-risk pivot diffuses awkward tension, improves the accuracy of your next skill, and puts the ball in your court as you ride the renewed flow steered to your advantage.  
(Ex: If the person starts talking about sports and you don’t play/like sports, shift the topic onto fitness instead if you like fitness
Ex 2: Someone starts talking about celebrity drama and you change the subject into talking about educational podcasts with popular writers
Ex 3: They talk about something you can’t relate to: “Can’t say I know much about that, but I’ve been working on improving my routine. What’s yours like?”).
Deals medium Gun damage.""")


commentary_jab = LightSkills("Commentary Jab", "Gun", "Light", "5%",
"""   - Fire off a swift, social shot that makes a brief observation about your surroundings. Useful for safely testing waters and opening dialogues. 
You can use it in the initial approach or early in conversations to gauge receptiveness and follow up with additional Gun skill combos or other elemental combo depending on if you get a 1 More. 
Ideal for public or casual settings where an overly direct approach might be inappropriate or awkward. Low-risk and easily recoverable if not reciprocated and naturally invites responses without pressure. 
(Ex: "This place is pretty packed today, huh?", 
Ex 2: “The music’s really good here. What are your thoughts on it?", 
Ex 3: "Looks like we're both stuck waiting for coffee huh?"
Ex 4: “I’m sure I’ll have my degree by the time this line ends”
Ex 5: “Seems like everyone’s in a rush today. Why do you think so?”
Ex 6: “I didn’t expect this place to smell so good– what’s cooking over there?”
Ex 7: “That guy’s cosplay is incredible. Have you seen anything like it before?”).
Deals light Gun damage. """)

binary_choice = LightSkills("Binary Choice", "Gun", "Light", "9%",
"""   - Fire off a clean, low-risk either-or question that trims the fat off the conversation and forces a quick read. 
Binary Choice narrows the target’s options, breaks hesitation, and gets passive or indecisive people actually committing to something—without making the interaction heavy. 
By presenting two simple questions, you force a quick pick and open a window for deeper conversation.  
(Ex: Would you say you’re more of a dog person or a cat person, and why?, 
Ex 2: "Would you say you’re more of an introvert or an extrovert, and why? ", 
Ex 3: "You more of a coffee or tea person, and why?"). 
Deals light Gun damage.""")

mood_check = LightSkills("Mood Check", "Gun", "Light", "5%",
"""   - A light, casual question aimed at gauging the target’s emotional state/energy without getting too personal and/or overstepping. 
It's subtle, friendly, and non-intrusive, letting you assess receptiveness before escalating the interaction. 
Perfect for opening moments, low-commitment conversation, or when someone’s energy seems off. 
(Ex: "You look kind of nervous. Everything good?"
Ex 2: "You seem kinda focused, everything cool?"
Ex 3: “How are you feeling today?”
Ex 4: “You seem to be in a good mood today. What’s making it a good one?”
Ex 5: “Feeling a bit tired today or just relaxed?”). 
Deals light Gun damage.""")

surface_graze = LightSkills("Surface Graze", "Gun", "Light", "5%",
"""   - Make a quick, neutral observation about a visible, surface-level aspect of the person: clothing, accessories, hairstyle, etc. 
It's a simple engagement tool that shows awareness without diving deep. If they respond positively, it opens the path for more personalized conversation. 
(Ex: "That's a cool jacket, where'd you get it?", 
Ex 2: "Your hair's got a really clean look. You do it yourself?", 
Ex 3: “Nice watch! Did you get it recently?”
Ex 3: "That sticker on your laptop is awesome! Where’d you get it?", 
Ex 4: "Is that a JJK sticker on your car? That's totally sick")
Ex 5: “Those sneakers are fresh– are they new?”).  
Deals light Gun damage. """)

mini_gun = LightSkills("Mini-Gun", "Gun", "Light", "6%",
"""   - Initiate small talk with the target. Mini-Gun is a low-risk entry conversation opener or gap-filler that, if they dive in, you know they're open to more personal talk. 
Great for initiating something bigger from something small if the target is receptive to it. 
This move can soften up your opponent for a 1 More + elemental follow up combo. 
(Ex: "Big weekend plans?"
 Ex 2: "Did you catch that game last night?"
 Ex 2: "How’s the work week been for you??"
 Ex 3: "Crazy weather today huh?"
 Ex 4: "Anyone tried that new coffee spot?"
 Ex 5: "Are you in college by any chance?"
 Ex 6: “How’s your shift been?”
 Ex 7: “How’s the work week been for you?”
 Ex 8: “What did you learn in class today?”
 Ex 9: When seeing a tall person: "You must get the ‘do you play basketball’ question a lot don't you?).
Deals light Gun damage.""")

starter_shot = LightSkills("Starter Shot", "Gun", "Light", "5%",
"""   - Launch a friendly, laid-back greeting accompanied by a warm smile and relaxed body language. 
This low-risk opener creates a safe, easy entry point for the start of a potential conversation. 
It signals friendliness, vibe testing, and if the target fires back and how they do. 
Ideal for warm-ups, first impressions, or feeling out a stranger’s receptiveness. 
(Ex: Hey, it's great to meet you", 
Ex 2: "Hey, how's it going"
Ex 3: “Hey, what’s up?”
Ex 4: “Hey! How’s it been?
Ex 5: “Yo, how’s your day been treating you?
Ex 6: “Hey, good to see you!”
Ex 7: “What’s up man”). 
Deals light Gun damage.""")

courtesy_shot = LightSkills("Courtesy Shot", "Gun", "Light", "6%",
"""   - Deliver a polished, respectful greeting that signals professionalism and courtesy. Your tone, phrasing, and demeanor convey respect, potentially creating a 1 More opportunity. 
Best used in offices, networking events, business-related inquiries, or any first-meet setting where respect and a good first impression opens doors. (Ex: "Good afternoon ma'am, it's great to see you", 
Ex 2: "Good evening sir, how are you?"
Ex 3: “Hello, it’s great to finally connect with you”
Ex 4: “Good morning! I’ve been looking forward to this meeting”
Ex 5: “Good afternoon, it’s a pleasure to speak with you today). 
Deals light Gun damage.""")

intent_snap = LightSkills("Intent Snap", "Gun", "Light", "6%",
"""   - Fire a subtle, non-confrontational question to quickly gauge someone’s intent, presence, or level of engagement. 
Delivered in a friendly, approachable tone, Extraction Shot gives the illusion of being helpful, but functions as a tactical scan for reading a person’s initial intent. 
Invites clarification and is great for dealing with socially ambiguous, passive, or nervous individuals.
(Ex: "Hey there, can I help you?"
Ex 2: "Looking for something?"
Ex 3: "You waiting on someone?"
Ex 4: "Everything alright?"
Ex 5: “You just browsing or waiting for someone in particular?”
Ex 6: “What’s up?”
Ex 7: “You seem a bit lost. Need help?”
Ex 8: “Is this your first time around here?”).
Deals light Gun damage.""")

echo_shot = LightSkills("Echo Shot", "Gun", "Light", "5%",
"""   - A low-investment countermeasure where you match someone's low effort, whether that's dry texts, weak replies, or passive energy so you can read their real interest without spending yours. 
By reflecting their vibe back exactly as it comes, you hold frame and gather intel on whether or not you should continue to invest in the conversation. 
Echo Shot is a troubleshooting move that gives the target an indirect chance to raise their energy if they actually care. If they don't you get an easy 1 More, allowing you to pivot into an All-Out Attack and cut things off without hesitation. 
(Ex: They text you: "lol", you reply: "lmao", 
Ex 2: They text you: "maybe idk", you reply: "gotchu, idk either"
Ex 3: They respond after 6 days with one word, you reply with also one word after a similar gap
Ex 4: They send a single emoji without elaborating, you send the same emoji back without elaborating 
Ex 5: They act dry, you act dry back). 
Deals light Gun damage.""")

subtext_bullet = LightSkills("Subtext Bullet", "Gun", "Light", "5%",
"""   - Plant a subtle cue that nudges someone toward a task or action without overt pressure or direction. 
Delivered naturally through clever phrasing or casual observation, this remark gently guides someone’s behavior while keeping the interaction low-risk and low-pressure.
(Ex: “It would be great if that report got finished soon”
Ex 2: “I wonder who’ll get that done first. It’d be impressive to see”
Ex 3: “It’d be awesome if someone tackled that thing today…”
Ex 4: “I’d love to see that handled sooner rather than later”
Ex 5: “It’d be nice to see that wrapped up before lunch. Just saying”
Ex 6: “Imagine how smooth the meeting will go once that’s done”).
Deals light Gun damage.""")

acknowledgement_shot = LightSkills("Acknowledgement Shot", "Gun", "Light", "5%",
"""   - Fire a low-risk opening to test whether the target is receptive enough to acknowledge your presence. 
This skill is used at the very start of an interaction to gauge baseline openness before committing further resources. 
A clear response (verbal or non-verbal) confirms basic receptiveness and unlocks follow-up actions. 
Lack of response, dismissive tone, or avoidance immediately ends the attempt with minimal cost, preventing wasted time and attention. 
This skill does not escalate—it strictly tests acknowledgment and availability.
(Ex: “Excuse me”
Ex 2: “Hey, excuse me”
Ex 3: “Hey”).
Deals light Gun damage.""")


severe_skills = ()
heavy_skills = (quick_probe)
medium_skills = (quick_invite, sniper_question, interest_probe, weekend_needle, soft_deflect, social_probe, subject_grenade)
light_skills = (commentary_jab, binary_choice, mood_check, surface_graze, mini_gun, starter_shot, courtesy_shot, intent_snap, echo_shot, subtext_bullet, acknowledgement_shot)


#GunSkills.display_skill(binary_choice)

#quick_invite = MediumSkills("")
