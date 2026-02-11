# Filename: Elec Skill List.py
# Date: 2/7/26
# Author: Aoi | shadowsnowwolf
# List of Elec skills (Wit/Humor)

class ElecSkills:
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

class SevereSkills(ElecSkills):
    pass

class HeavySkills(ElecSkills):
    pass

class MediumSkills(ElecSkills):
    pass

class LightSkills(ElecSkills):
    pass

example = LightSkills("X", "Elec", "Light", 0,
"""   - X""")

# Heavy Damage Grade Skills
lightning_retort = HeavySkills("Lightning Retort", "Elec", "Heavy", 13,
"""   - A sharp, surgical comeback that cuts deep into the target's ego, delivering a heavy confidence and ego blow. Effective against overconfident, condescending targets, or those who try to make you less than you are. 
(Ex: Them: *Dismisses your idea* "Sure, good luck making that happen." You: "Right, because your track record speaks for itself" 
Ex 2: Them: “You’ll never pull that off.” You: “Says the CEO of losers”
Ex 3: Them: “You’re not as impressive as you think” You: “And yet somehow, I’m still more memorable than you”
Ex 4: Them: “Why are you even here? This is way out of your league” You: “I belong where I want NPC”)
Ex 5: Them: “Look at how skinny you are. You’re like a twig” You: “Says the professional donut eater trying to lecture me on weight.
Ex 6: Them: “You’re not really my type.” You: “Awesome. I’d hate to blend in with the rest of your orbiter fan club”  
Ex 7: Them: “Why are you even talking to me? I’m out of your league” You: “My bad for not giving a f***”
Ex 8: Them: “I’m pretty, and you’re ugly” You: “You’re a 3 on a good day”).
Deals heavy Elec damage.""")

verbal_parry = HeavySkills("Verbal Parry", "Elec", "Heavy", 12,
"""   - A witty, playful deflection that treats the target’s jab as inconsequential. It uses wit and light sarcasm while maintaining your frame and flipping the ego damage on the target instead. Perfect for handling insults, shit-tests, and ego checks using humor and wit to defuse their strike without losing composure. Even harsh digs and insults can be spun into a clever response that projects confidence and unpredictability, turning their attempt to cut you down into fuel for your spark. 
(Ex: Them: "Wow, you're kinda full of yourself." You: "Not my fault that I’m as confident as I am." 
Ex 2: Them: “You’re ugly.” You: “I’m so hurt. Grab a mirror silly” Wave them off 
Ex 3: Them: “You must think you’re special.” You: “Oh, I know I’m special.”
Ex 4: Them: “No one likes you” You: “And your opinion will matter once flying cars are a thing” 
Ex 5: Them: “You really think people take you seriously?” You: “Clearly you did, since I took up enough mental bandwidth in your mind that you felt the need to ask.”
Ex 6: Them: "Oh, so you're an expert now? You: "Expert? Only at spotting weak comebacks"
Ex 7: Them: "You really think that shirt suits you?"  You: "Better than your choice of opinions"
Ex 8: Them: “That haircut looks like shit on you.” You: “You’re just jealous that I could pull it off way better than you ever could”).
Deals heavy Elec damage. """)


# Light Damage Grade Skills
shocking_humor = LightSkills("Shocking Humor", "Elec", "Light", 5,
"""   - Deliver sharp, situational humor that highlights absurdity, irony, or exaggeration in everyday life. Perfect for observational or sarcastic jokes that draw attention and spark reactions without being directed at anyone personally. Works best as a standalone comment or reflection on a situation, showing wit and cleverness. Can create a 1 More by eliciting laughter or playful engagement.
(Ex: "I'm not saying I'm dramatic, but if I trip in public, I'm staying down until someone calls an ambulance." 
Ex 2: "I flirt like a broken vending machine, a lot of energy for unpredictable results." 
Ex 3: "I put off all the things I could do today… except procrastinating. I nailed that"
Ex 4: “Don’t bring me near computers unless you want your whole office setup to short-circuit”
Ex 5: “I have a love-hate relationship with mornings… mostly hate.”
Ex 6: “If there was a reward for overthinking I’d reach a guinness world record”). 
Deals light Elec damage.""")

current_confirmaiton = LightSkills("Current Confirmation", "Elec", "Light", 3,
"""   - A sly, lightning-quick reframing jab that playfully interprets the target’s hesitation, half-answers, indirect agreements, or non-committal answers as agreement. This move jolts the social tempo by converting ambiguity into momentum, teasing them into engagement without pressure. Perfect for keeping the vibe light, witty, and confidently forward.
(Ex: "You blinked. That counts as a response" 
Ex 2: "I speak fluent sarcasm. That was a yes, right?"
Ex 3: “I’ll take that maybe as a yes”
Ex 4: “That maybe sounded like a yes to me”
Ex 5: “Your silence speaks volumes you know”
Ex 6: “You didn’t say no, which scientifically means yes”
Ex 7: “Blink twice if you agree. Welp, looks like we have our answer.”).
Deals light Elec damage.""")

sonic_quip = LightSkills("Sonic Quip", "Elec", "Light", 4,
"""   - A sharp, reactive one-liner that sparks with playful wit. Used to flip comments, banter, or awkward remarks into humor in the moment, showing fast reflexes and clever timing. Best used when the other person gives you something to bounce off of. 
(Ex: Them: “That’s kind of random.” You: “So am I. Guess I’m like a lucky dice huh?”
Ex 2: Them: “You’re late.” You: “Perfect timing. I arrived exactly when the plot needed me”
Ex 3: Them: “You’re late” You: “Stylishly if I might add”
Ex 4: Them: “You’re late” You: “Yep. And with style”
Ex 5: Them: “You look tired” You: “Yeah… coffee and I are negotiating”).
Deals light Elec damage.""")

deadpan_discharge = LightSkills("Deadpan Discharge", "Elec", "Light", 5,
"""   - Respond to a comment, observation, or situation with flat, ironic, or sarcastic humor. Can spark laughter, catch people off guard, and test social receptiveness while signaling wit and cleverness. Can create a 1 More by disarming tension, drawing the target into playful engagement, making the target laugh, or creating a reaction within them.
(Ex: Them: “I burned dinner again” You: “Nice. Was the fire department impressed this time?”
Ex 2: Them: “I overspent shopping again” You: “Wow, I’m surprised your bank account hasn’t submitted a complaint for domestic abuse yet”
Ex 3: Them: “I procrastinated again” You: “Shocking. I never would have guessed that your future self hates you.”
Ex 4: Them: “My phone died” You: “Should we prepare the burial?”
Ex 5: Them: “I couldn’t stop myself from buying those shoes in the mall” You: "And this is the part where you want me to emotionally support your shopping addiction huh?").
Deals light Elec damage.
""")

volt_revive = LightSkills("Volt Revive", "Elec", "Light", 4,
"""   - A quick, witty comment or offbeat question that revives a stalled or low-energy conversation, injecting immediate humor and momentum. Perfect for breaking awkward silences or lifting dying interactions.
(Ex: "If a zombie apocalypse were to happen right now, who do you think is dying first?" 
Ex 2: "Okay, what's the weirdest thing you've Googled this week?"
Ex 3: “If your cat could talk, what do you think it would be saying to you on a daily basis?”)
Ex 4: “If we pulled up your browsing history right now, what do you think we would find?). 
Deals light Elec damage. """)


severe_skills = ()
heavy_skills = (lightning_retort, verbal_parry)
medium_skill = ()
light_skills = (shocking_humor, current_confirmaiton, sonic_quip, deadpan_discharge, volt_revive)
