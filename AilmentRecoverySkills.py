# Filename: AilmentRecoverySkills.py
# Date: 5/28/26
# Author: Aoi | shadowsnowwolf
# List of Status Ailment Recovery skills


class AilmentRecoverySkills:
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

    # Shows the simplified info of the skill
    def display_simplified_info(self):
        print(f"{self.name} ({self.type})")

# Example:
#ex = AilmentRecoverySkills("","Ailment Recovery", 12, 
#"""                           """)

frame_reset = AilmentRecoverySkills("Frame Reset","Ailment Recovery", 12, 
"""    - Cure Confusion by re-aligning perception with objective reality and reestablishing a shared frame. This skill stabilizes interpretation by separating facts from assumptions, clarifying intent, and discarding contradictory or misleading inputs. Scrambled reactions settle as rhythm normalizes, self-sabotage stops, and accuracy returns. Confusion collapses not through argument, but through clarity and grounding.
Ex mentality: "What do I actually know for sure right now?"
Ex mentality 2: "Strip out interpretations—what was literally said or done?"
Ex mentality 3: "I might be mixing signals. Reset to observable facts."
Ex mentality 4: "One frame, one meaning. No doubles."
Cures Confusion for one ally.""")

hazard_audit = AilmentRecoverySkills("Hazard Audit","Ailment Recovery", 12, 
"""    - Break the fear response by deliberately reassessing the perceived threat through reality testing and proportional thinking. You identify what can actually happen, what you can control, and what the next safe action is, collapsing imagined danger back into manageable risk. Fear dissolves not through reassurance, but through accurate threat calibration.
Ex mentality: "What is the worst realistic outcome-- and can I survive it?"
Ex mentality 2: "What part of this is danger, and what part is anticipation?"
Ex mentality 3: "One step forward is safer than freezing"
Cures Fear for one ally.""")

temper_drop = AilmentRecoverySkills("Temper Drop","Ailment Recovery", 12, 
"""    - Consciously release resentment by choosing to forgive the person who triggered your anger—not to excuse their behavior, but to sever the emotional hold it has over you. By reframing the offense as information rather than injury, you reclaim control of your emotional state and dissolve the Rage status without escalation or suppression. Forgiveness here is an internal decision, not reconciliation. No apology or resolution from the other party is required. Cures the Rage status for one ally. 
Ex mentality : "They crossed a line, but I'm not letting it run my nervous system"
Ex mentality 2: "I'm done carrying this. I've already learned what I needed"
Cures Rage for one ally.""")

purpose_anchor = AilmentRecoverySkills("Purpose Anchor","Ailment Recovery", 12, 
"""    - Collapse Despair by forcibly reconnecting the target to a concrete reason to act—a responsibility, chosen identity, unfinished path, or near-term objective. Rather than generating optimism, this skill restores willpower by reestablishing meaning and direction. SP bleed stops immediately as purpose replaces nihilism; initiative and presence stabilize as action becomes justified again.
Ex mentality: "What is the worst realistic outcome-- and can I survive it?"
Ex mentality 2: “If nothing mattered, I wouldn’t be here deciding—so what’s the next step?”
Ex mentality 3: “I don’t need hope. I need a reason. This is it.”
Ex mentality 4: “Even if I feel empty, this task still needs to be done.”
Ex mentality 5: “I’m allowed to feel nothing and still move forward.”
Cures Despair for one ally.""")

autonomy_reclamation = AilmentRecoverySkills("Autonomy Reclamation","Ailment Recovery", 12, 
"""    - Reassert authorship of thought by identifying and rejecting externally installed narratives, whether imposed by individuals, groups, institutions, media, or culture at large. You consciously separate what you were taught to think from what you have personally verified, dissolving guilt hooks, fear framing, moral pressure, herd logic, and authority bias. This skill restores mental sovereignty by replacing borrowed conclusions with first-principles reasoning.
Ex mentality: "Who benefits if I believe this?"
Ex mentality 2: "Did I arrive at this conclusion or did I inherit it?"
Ex mentality 3: "This is a narrative, not a fact"
Ex mentality 4: "Authority isn't evidence"
Cures Brainwash for one ally.""")

attention_snap = AilmentRecoverySkills("Attention Snap","Ailment Recovery", 12, 
"""    - Cure Sleep by deliberately reasserting your own (or an ally’s) awareness and presence in the interaction. This skill interrupts zoning out, passive nodding, and avoidance by consciously pulling attention back into the moment and recommitting to engagement. HP regeneration from disengagement ends as responsiveness, initiative, and participation are restored. Sleep breaks through self-directed wakefulness, not external pressure.
Ex mentality: “I’ve been checked out—refocus.”
Ex mentality 2: “I’m drifting. Eyes up. Stay here.”
Ex mentality 3: “I need to be present for this—no autopilot.”
Ex mentality 4: “Pause distractions. Re-enter the conversation.”
Ex mentality 5: “I’m here now. Let’s continue.
Cures Sleep for one ally.""")

recall_thread = AilmentRecoverySkills("Recall Thread","Ailment Recovery", 12, 
"""    - Cure Forget by reconstructing the lost mental thread and restoring access to stalled skills. This skill stabilizes nerves, reduces cognitive overload, and re-centers attention on the last known anchor point (intent, goal, or prior thought), allowing momentum to resume. Skill lock is lifted as clarity replaces pressure-induced blanking, and conversational or action flow restarts cleanly instead of forcing improvisation under panic.
Ex mentality: “What was I trying to do here—one step back.”
Ex mentality 2: “Breathe. Resume from the last clear point.”
Ex mentality 3: “I don’t need the whole plan—just the next line.”
Ex mentality 4: “Slow it down. I remember what matters.”
Ex mentality 5: “Reset. Continue.”
Cures Forget for one ally.""")


singular_ailment_recovery_skills = (frame_reset, hazard_audit, temper_drop, purpose_anchor,
                                    autonomy_reclamation, attention_snap, recall_thread)
aoe_ailment_recovery_sklils = ()
all_ailment_recovery_skills = ()
