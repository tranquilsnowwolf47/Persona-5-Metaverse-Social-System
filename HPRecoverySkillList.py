# Filename: HPRecoverySkillList.py
# Date: 2/19/26
# Author: Aoi | shadowsnowwolf
# List of HP (Social Stamina) recovery skills

class HPRecoverySkills:
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


#example = LightRecoverySkills("X", "Light HP Recovery", 0,
#"""   - X""")

class LightRecoverySkills(HPRecoverySkills):
        pass

class ModerateRecoverySkills(HPRecoverySkills):
        pass

class FullRecoverySkills(HPRecoverySkills):
        pass


# Light HP Recovery Skills
twin_breath = LightRecoverySkills("Twin Breath", "Light HP Recovery", 3,
"""   - Rapidly reset your nervous system through a controlled double inhale and extended exhale, immediately lowering stress and stabilizing your composure. 
Inhale deeply through your nose, take a second short inhale to fully expand the lungs, then release a long, slow exhale through your mouth until empty. 
Repeat 3 times for one cast. 
The technique is based on physiological sighing, and executed outside of combat, or subtly during combat through attentive listening, brief pauses, relaxed posture, and measured speech to avoid suspicion from the Shadow.
Restores a small amount of HP (15%). """)

centered_breathing = LightRecoverySkills("Centered Breathing", "Light HP Recovery", 3,
"""   - Maintain composure and reduce ongoing stress by controlling your diaphragm. Inhale deeply into your abdomen, exhale slowly, and keep your posture relaxed. 
his subtle, continuous breathing restores a small amount of HP over time, helping prevent minor attrition from repeated social pressure. 
Repeat 3 times for one cast. 
Can be used during interactions without drawing attention. Based on belly breathing. 
Restores a small amount of HP (15%).""")

charged_breathing = LightRecoverySkills("Charged Breathing", "Light HP Recovery", 4,
"""   - Calm your nervous system instantly by focusing solely on long, controlled exhales. 
Let the air leave your lungs fully while allowing inhalation to occur naturally and unconsciously. 
This subtle technique lowers heart rate, stabilizes stress, and maintains composure during tense Palace encounters. Repeat 3 times for one cast. 
Can be used mid-interaction without drawing attention from Shadows. 
Restores a small amount of HP (18%).""")


# Moderate HP Recovery Skills
focused_breathing = ModerateRecoverySkills("Focused Breathing", "Light HP Recovery", 6,
"""   - Calm yourself down and lower your heart rate through deliberate breathing, reducing minor stress and regaining a small amount of HP. 
In this skill, you slowly inhale through your nose, and let out a long exhale through your mouth. 
Inhale for 4 seconds through your nose, hold for 1 second, and then exhale 3 seconds out through your mouth. Repeat 3 times for one cast. 
The skill is performed in a subtle and natural way through listening, pausing, smiling, and speaking to reduce suspicion from the Shadow. 
Restores a moderate amount of HP (35%).""")

cognitive_reframe = ModerateRecoverySkills("Cognitive Reframe", "Moderate HP Recovery", 6,
"""   - Actively recall and apply pre-learned rejection reframes and positive affirmations from memory to neutralize stress responses and restore emotional stability. 
Instead of relying on external tools or scripted content, you internally retrieve grounding statements and perspectives that reduce emotional weight and reframe negative or draining experiences. 
This process stabilizes self-perception, reduces rumination, and restores social stamina by shifting interpretation of events rather than suppressing them. 
Requires conscious recall and intentional application, making it an active cognitive recovery skill rather than passive relaxation.
Restores a moderate amount of HP (35%).""")

cat_nap = ModerateRecoverySkills("Cat Nap", "Moderate HP Recovery", 6,
"""   - A brief power nap that channels mental focus into rapid rest. 
In just minutes, you awaken refreshed, your body’s stamina restored as though you’d slept for hours. 
Can only be used outside an encounter (you can’t nap in the middle of a conversation). 
Restores a moderate amount of HP (35%).""")

white_reset = ModerateRecoverySkills("White Reset", "Moderate HP Recovery", 6,
"""   - Intentionally restore mental stability by creating or accessing a continuous white noise environment, using it to reduce cognitive load and lower stress arousal. 
This can be done by playing white noise directly or mentally simulating a uniform auditory field while focusing on breath and posture. 
The process dampens overstimulation, clears emotional noise, and resets baseline tension. 
Requires deliberate setup or recall before activation, making it a conscious recovery action rather than an automatic effect.
Restores a moderate amount of HP (35%).""")

sage_stillness = ModerateRecoverySkills("Sage Stillness", "Moderate HP Recovery", 7,
"""   - Deliberately enter a controlled meditative state to reduce mental noise, lower physiological stress, and restore social stamina. 
Attention is narrowed through breath awareness, posture stabilization, and passive observation of thoughts without engagement. 
This process reduces emotional reactivity and resets baseline tension, allowing for steady recovery of HP. 
The skill can be performed subtly in low-stimulation environments or briefly during pauses in interaction without drawing attention.
Restores a moderate amount of HP (40%).""")


# Full HP Recovery Skills
concentrated_breathing = FullRecoverySkills("Concentrated Breathing", "Full HP Recovery", 18,
"""   - Calm yourself with slow, deliberate breaths and focused body awareness, reducing stress and tension while regaining a meaningful amount of HP. 
Inhale through your nose for 4 seconds, hold for 4 seconds and then, exhale slowly through your mouth for 5 seconds. Repeat 8 times per cast. 
Maintain relaxed posture and controlled movements throughout, letting your mind and body reset naturally. 
Fully restores HP (100%). """)

laughter_trigger = FullRecoverySkills("Laughter Trigger", "Full HP Recovery", 18,
"""   - Intentionally induce sustained, genuine laughter to fully reset your emotional and physiological state. 
This requires committing to a strong enough stimulus—internal or external—to produce continuous, real laughter rather than a brief reaction. 
The effect only completes if the laughter is maintained long enough to fully dissipate stress, making the recovery dependent on execution quality rather than instant activation. 
Short or forced reactions will fail to produce full recovery.
(Ex: watching a funny video long enough to genuinely laugh multiple times
Ex 2: engaging with humor until you feel a noticeable emotional reset
Ex 3: allowing yourself to fully react instead of suppressing laughter
Ex 4: staying with the stimulus until tension is clearly gone
Ex 5: replaying or continuing until the response is sustained, not momentary
Ex 6: reaching a point where your breathing and mood have visibly shifted).
Fully restores HP (100%).""")


light_recovery_skills = (twin_breath, centered_breathing, charged_breathing)
moderate_recovery_skills = (focused_breathing, cognitive_reframe, cat_nap, white_reset, sage_stillness)
full_recovery_skills = (concentrated_breathing, laughter_trigger)
