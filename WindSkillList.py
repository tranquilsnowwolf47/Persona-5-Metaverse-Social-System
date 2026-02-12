# Filename: WindSkillList.py
# Date: 2/10/26
# Author: Aoi | shadowsnowwolf
# List of Wind skills (Curiosity/Connection)

class WindSkills:
    def __init__(self, name, element, damage_grade, SP_cost, description): # Constructor
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


class SevereSkills(WindSkills):
    pass

class HeavySkills(WindSkills):
    pass

class MediumSkills(WindSkills):
    pass

class LightSkills(WindSkills):
    pass

# Heavy Skills
everflow = HeavySkills("Everflow", "Wind", "Heavy", 14,
"""   - Anchors you fully in the present moment and dissolves overthinking restoring natural conversational flow. 
As long as the user remains present and curious, each exchange organically creates the next. 
Silences stop being threats and become openings, allowing conversation to continuously regenerate. 
By focusing on what’s happening right now, you never run out of things to say. Everflow doesn’t rely on scripts– it turns attention into infinite material. 
Excels in first meetings, dates, interviews, and long conversations. 
(Ex: Them: “This place is kinda crowded” You: “You: “Yeah—do you usually like busy spots, or are you more low-key?”).
Deals heavy Wind damage.""")

tailwind_cascade = HeavySkills("Tailwind Cascade", "Wind", "Heavy", 14,
"""   - Deploy a layered chain of follow-up questions that compounds momentum, actively cycles the conversation toward higher-value topics, and stress-tests interest and alignment. 
Each follow-up builds on the last response, increasing clarity while keeping flow natural and pressure low.
(Ex: "What part of the work actually keeps you busy?"
Ex 2: “What would you rather be doing if time wasn’t the issue?”
Ex 3: “So what made you come down to Florida?”
Ex 4: “Do you usually train alone or with people?”
Ex 5: “What part of work actually drains you the most?”
Ex 6: “Is that something you chose or something you feel into?”). 
Deals heavy Wind damage.""")


# Medium Skills
callback_gale = MediumSkills("Callback Gale", "Wind", "Medium", 7,
"""   - Deliberately reference a personal detail they mentioned previously to bring new potential conversation topics into the mix. 
You can use it when you've had at least one back-and-forth. 
For example, if earlier they said they love weekend hikes, bring it up again when you shift topics to lead into new social territory. 
(Ex: "Last week, you mentioned how much you love weekend hikes. What are your favorite trails to go on and why?"
Ex 2: “You mentioned earlier that you’re learning guitar. What’s your practicing process look like?”
Ex 3: “You said you’ve been binge-watching a series. Are you keeping up with it now, or have you switched to something else?”). 
Deals medium Wind damage. """)

deep_dive = MediumSkills("Deep Dive", "Wind", "Medium", 8,
"""   - Follow up after sensing shared interest, asking a more specific, layered question that invites the other person to share opinions, stories, or insider takes. 
This is the moment where you move past surface-level curiosity and genuinely explore their world. 
Effective to use after Interest Probe (Gun) lands and they show passion or familiarity with a topic. 
Can also be used when you want to deepen connection and get them talking more meaningfully, as well as when you're ready to trade stories or show that you see them. 
(Ex 1: "Okay, so what's your hot take on the new season?", 
Ex 2: "You've been to a few cons, right? What's your favorite experience so far?", 
Ex 3: "You like Persona 5? Who’s your favorite character?"). 
Deals medium Wind damage. """)

entry_path = MediumSkills("Entry Path", "Wind", "Medium", 8,
"""   - Guide the conversation toward how you could personally get started in a skill, hobby, or field that the target is knowledgeable or experienced in. 
By positioning them as a reference point or informal guide, you invite practical advice, step-by-step explanations, and natural teaching energy. 
This builds connection through curiosity, respect, and shared interests while keeping the conversation active and forward-moving.
(Ex: “How could I get started with cosplay customization?”
 Ex 2: “If I wanted to learn that from scratch, what would you recommend first?”
 Ex 3: “What’s the easiest entry point for someone new to this?”
 Ex 4: “Are there any beginner mistakes I should avoid when starting?”
 Ex 5: “What tools or skills would I need early on?”
 Ex 6: “If you were starting over today, what would you do differently?”
Ex 7: “If you could relearn coding from the beginning what would you do differently?”
Ex 8: “If I wanted to learn how to code, how would you recommend I start?”).
Deals medium Wind damage. """)

depth_anchor = MediumSkills("Depth Anchor", "Wind", "Medium", 9,
"""   - Ask the target for their reasoning for getting into an action, goal, interest, or thing. 
This shifts conversation from “what” and “how” into identity-level insight, naturally opening storylines, emotions, and value alignment, and getting the user to open up on their reasoning.
(Ex 1: “What made you want to study biomedical sciences?”
Ex 2: "“What pushed you to choose that path instead of the others?”
Ex 3: "What made you choose that specific sport over others?"
Ex 4: “What made you choose IT over software engineer?”). 
Deals medium Wind damage. """)

career_current = MediumSkills("Career Current", "Wind", "Medium", 7,
"""   - Guide the conversation toward someone’s occupation, career path, or professional goals in a natural, curious way. 
Thoughtful questions reveal their ambitions, values, and work habits, while showing genuine interest. 
This builds connection, encourages sharing, and gives you meaningful insight into their priorities.
(Ex: “What got you interested in that field?”
 Ex 2: “Is there a project or goal you’re really excited about right now?”
 Ex 3: “Where do you see yourself in 5 years from now in this career path?” 
 Ex 4: “What skills are you hoping to build in the next year for the workforce?”
 Ex 5: “Do you see yourself sticking with this career long-term or exploring other paths?”
Ex 5: “So what do you do for work?”
Ex 6: “What kind of job are you looking for after graduation?”).
Deals medium Wind damage.""")

mind_glide = MediumSkills("Mind Glide", "Wind", "Medium", 7,
"""   - Shift across various social topics, even ones you're not deeply familiar with to keep the conversation flowing and show a genuine willingness to learn. 
Demonstrates social adaptability and interests in other's worlds, and may open up windows for mutual connection if you discover a mutual interest. 
Can also be used to shift topics if the current topic is fizzling out or getting awkward, or also when you notice someone is quiet about the topic so you decide to shift to something they may be more able to contribute to. 
(Ex: "I'm not super familiar with that, but it sounds cool. How does it work?", 
Ex 2: "I've never really gotten into that, but it sounds interesting. What do you like about it?"). 
Deals medium Wind damage. """)

thought_unravel = MediumSkills("Thought Unravel", "Wind", "Medium", 8,
"""   - Ask a sincere, open-ended question that gently pulls at the threads of someone's thoughts, encouraging them to reflect or open up. 
Ideal for deepening connection or drawing insight from a shadow. 
(Ex: “What does that mean to you?” 
Ex 2: “How did that change the way you see things?
Ex 3: “So what’s your take on this situation?”).
Deals medium Wind damage.""")

winds_of_knowledge = MediumSkills("Winds of Knowledge", "Wind", "Medium", 7,
"""   - Share something you're genuinely knowledgeable about when it fits the moment, using your insight to enrich the conversation and spark connection. 
If a topic is brought up, you can explain more about that topic in a way that's educational and fulfilling to the conversation. 
It’s not about showing off, but giving value and sparking conversation.
(Ex: If someone mentions having poor social skills and you have good social skills, you can teach them some techniques that they may come to appreciate and can build rapport). 
Deals medium Wind damage.""")

# Light Skills 
inquisitive_breeze = LightSkills("Inquisitive Breeze", "Wind", "Light", 4,
"""   - Show genuine curiosity and interest towards the target. 
By openly expressing interest, you prompt the Shadow to reveal deeper insights into their personality, motivations, and goals if they reciprocate. 
(Ex: "I'd love to hear more about your trip"
Ex 2: “Please—tell me more about that”
Ex 3: “I’m listening”).
Deals light Wind damage.""")

severe_skills = ()
heavy_skill = (everflow, tailwind_cascade)
medium_skills = (callback_gale, deep_dive, entry_path, depth_anchor, career_current, mind_glide, thought_unravel, winds_of_knowledge)
light_skills = (inquisitive_breeze)
