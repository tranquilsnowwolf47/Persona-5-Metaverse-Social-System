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
"""    - Realign perception by filtering reality through observable facts instead of assumptions, emotional noise, or social pressure. Frame Reset restores cognitive stability by separating what is known from what is inferred, allowing clear judgment to replace distorted interpretation. Contradictory signals lose their influence as attention returns to objective evidence and deliberate choice.
Trigger cue:
Look at your fingers, inhale in deeply, and snap your fingers all at once to stop your current train of thought. Attention shifts away from overthinking and opens the way for the next step, that being the cognitive reframe. A finger snap acts as a conditioned cue that immediately brings awareness to the presence of Confusion. It interrupts the current thought loop, breaks automatic reactions, and creates a brief moment of mental separation from the distortion.
After the finger snap, use short objective reasoning to separate reality from overthinking and regain cognitive clarity.
Ex: Social Pressure
A crowd disagrees with your decision and you begin doubting yourself. Frame Reset separates the crowd’s opinion from what actually happened, allowing you to decide whether your judgment should change based on the situation itself rather than the audience’s reaction.
Ex 2: Mixed Signals
Someone’s words and actions don’t seem to match. Frame Reset separates what was directly said from what was directly done, removing the urge to fill in the gaps until more information is available.
Ex 3: Information Overload 
Too many opinions, advice, or inputs leave you mentally scattered. Frame Reset filters out everything that isn’t relevant to your current objective, leaving only the information needed to move forward.
Ex 4: Assumed Intent
You begin believing you know what someone else meant or was thinking. Frame Reset removes conclusions that aren’t directly supported and returns your attention to what was actually communicated.
Ex 5: Emotional Distortion 
Strong emotions begin changing how you see the situation. Frame Reset recognizes the emotion without letting it define reality, then reassesses the situation using what actually occurred.
Ex 6: Public Evaluation
Praise, criticism, rejection, or applause begins affecting your judgment. Frame Reset separates external feedback from your own standards, allowing you to evaluate the feedback on its own merits instead of automatically accepting or rejecting it.
Ex 7: Decision Paralysis
Too many possible interpretations leave you unable to act. Frame Reset removes unsupported possibilities, keeps the interpretations that have the strongest support, and identifies the next clear action.
Cures Confusion for one ally.""")

hazard_audit = AilmentRecoverySkills("Hazard Audit","Ailment Recovery", 12, 
"""    - Break the fear response by deliberately reassessing the perceived threat through reality testing and proportional thinking. Hazard Audit restores composure by separating realistic danger from anticipated harm, allowing deliberate action to replace avoidance and self-suppression. Instead of reacting to what might happen, you determine what is actually happening, what is realistically at risk, what remains within your control, and what the next safe action is. As exaggerated threats lose their influence, confidence and independent action gradually return.
Trigger cue:
Rub the inside of your wrist where your pulse can be felt while taking a slow breath. The movement acts as a conditioned cue that immediately brings awareness to the presence of Fear, interrupting spiraling anticipation, intimidation, and automatic compliance. Feeling your pulse serves as a reminder that your body has entered a threat-response state, but that physiological activation alone does not confirm actual danger. The cue creates a brief moment of separation between feeling afraid and being in danger.
After the cue, deliberately reassess the situation by identifying what you are realistically afraid will happen, how likely that outcome truly is, whether you could handle it if it occurred, and what safe action remains available to you right now. By distinguishing genuine threats from perceived ones, fear loses its ability to dictate behavior and deliberate action becomes possible again.
Ex 1: Social Intimidation
Someone with strong presence, status, or confidence makes you second-guess yourself and become quieter. Hazard Audit separates their intimidating presence from your actual safety, allowing you to continue expressing yourself.
Ex 2: Fear of Rejection
You want to approach someone, voice an opinion, or take initiative but become preoccupied with being judged or rejected. Hazard Audit recognizes that discomfort and embarrassment are not the same as genuine danger.
Ex 3: Hostile Energy
Someone behaves aggressively or confrontationally, causing you to withdraw or become overly cautious. Hazard Audit determines whether the situation requires genuine caution or whether your fear response is exaggerating the threat.
Ex 4: Group Pressure
You privately disagree with others but feel pressured to conform in order to avoid attention or exclusion. Hazard Audit evaluates whether disagreement would realistically result in meaningful harm.
Ex 5: Fear of Failure
You avoid taking action because you are afraid of making mistakes or embarrassing yourself. Hazard Audit reframes failure as manageable information rather than catastrophic danger.
Ex 6: Walking on Eggshells
You become hypervigilant around an intimidating person and begin suppressing your personality or opinions to avoid conflict. Hazard Audit assesses whether the perceived threat justifies the level of self-suppression being displayed.
Ex 7: Hesitation Under Pressure
Fear causes you to freeze, overthink, and delay action despite wanting to act. Hazard Audit identifies the next safe and manageable step, restoring momentum and initiative.
Cures Fear for one ally.""")

temper_drop = AilmentRecoverySkills("Temper Drop","Ailment Recovery", 12, 
"""    - Restore emotional regulation by consciously releasing the need for retaliation, vindication, or immediate emotional discharge. Temper Drop does not deny anger or pretend that the offense did not occur. Instead, it acknowledges the emotional injury while choosing not to let it dictate behavior. By reframing the event as information rather than a personal threat that must be acted upon, emotional intensity loses its grip and rational control returns. Forgiveness here is an internal act of letting go, not excusing behavior or reconciling with the other person. Rage dissolves as emotional energy is redirected away from escalation and back toward deliberate choice.
Trigger cue:
Look at your hand, slowly clench your fist, hold it briefly, and then gradually open it. The movement acts as a conditioned cue that immediately brings awareness to the presence of Rage, interrupting automatic escalation and impulsive reactions. The clenched fist acknowledges the anger instead of suppressing it, while opening the hand symbolizes releasing the urge to retaliate or remain emotionally attached to the offense. Attention shifts away from the provoking stimulus and back toward yourself, creating a brief moment of separation from the emotion.
After opening your hand, identify what boundary was crossed or what lesson the anger is revealing. Then determine whether holding onto the emotional charge is still useful. Once the information has been extracted, consciously release the resentment and choose your next action deliberately rather than reacting impulsively.
Ex 1: Humiliation
Someone embarrasses you publicly, causing wounded pride and an urge to retaliate. Temper Drop acknowledges the hurt while refusing to let humiliation control your behavior.
Ex 2: Disrespect
Someone speaks to you rudely or crosses a boundary. Temper Drop separates the boundary violation from the emotional urge to immediately strike back, allowing you to respond strategically instead of impulsively.
Ex 3: Repeated Frustration
Obstacles or repeated failures begin building emotional pressure. Temper Drop releases accumulated resentment before it escalates into aggression or self-destructive behavior.
Ex 4: Betrayal
Someone violates your trust and anger begins consuming your thoughts. Temper Drop extracts the lesson from the experience while letting go of the need for emotional revenge.
Ex 5: Argument Escalation
You feel yourself becoming louder, more confrontational, and increasingly reactive during conflict. Temper Drop interrupts the escalation cycle and restores emotional composure.
Ex 6: Wounded Pride
Criticism or failure exposes an insecurity and creates an urge to defend your ego aggressively. Temper Drop acknowledges the emotional pain without allowing pride to override good judgment.
Ex 7: Desire for Retaliation
You become fixated on proving a point, getting even, or making someone feel what you felt. Temper Drop releases the need for emotional repayment and redirects attention toward your long-term interests.
Cures Rage for one ally.""")

purpose_anchor = AilmentRecoverySkills("Purpose Anchor","Ailment Recovery", 12, 
"""    - Collapse Despair by reconnecting the target to a concrete reason to continue acting, whether it be a responsibility, value, relationship, goal, chosen identity, or unfinished path. Purpose Anchor does not attempt to create artificial optimism or deny emotional pain. Instead, it restores willpower by re-establishing meaning, direction, and personal investment in the future. Despair weakens as the target remembers that emotional exhaustion does not invalidate purpose and that meaningful action remains possible even in the absence of hope. SP deterioration stabilizes as initiative, presence, and engagement gradually return.
Trigger cue:
Place your hand over your heart or pec area, gently squeeze, and take a slow inhale. The movement acts as a conditioned cue that immediately brings awareness to the presence of Despair, interrupting emotional numbness, apathy, and the urge to emotionally withdraw. The squeeze symbolizes reconnecting with your inner values, desires, and reasons for continuing, while the inhale re-engages you with the present moment. The cue creates a brief moment of separation from nihilistic thinking and reminds you that emotional emptiness does not mean that meaning itself has disappeared.
After the cue, deliberately identify something that still matters to you, no matter how small. This may be a responsibility, a person, a promise, a value, an unfinished goal, or simply the next step that still deserves your attention. Rather than asking whether you feel motivated, determine whether there is still a reason to continue moving forward. By reconnecting with meaning instead of waiting for motivation, initiative and emotional engagement gradually return.
Ex 1: Repeated Failure
After numerous setbacks, you begin believing that further effort is pointless. Purpose Anchor reconnects you with why you started and identifies a reason to continue despite discouragement.
Ex 2: Burnout
Prolonged stress and exhaustion leave you emotionally numb and disconnected from your goals. Purpose Anchor restores direction by focusing on what still matters rather than how motivated you currently feel.
Ex 3: Existential Hopelessness
You begin questioning the value of effort, progress, or life direction itself. Purpose Anchor shifts attention away from abstract hopelessness and toward concrete sources of meaning and responsibility.
Ex 4: Emotional Defeat
Repeated rejection or disappointment causes you to emotionally check out and stop caring about outcomes. Purpose Anchor reminds you that pain and meaning can coexist, allowing engagement to gradually return.
Ex 5: Giving Up Mid-Effort
You suddenly lose the desire to continue a task, conversation, or pursuit and begin thinking, “What’s the point?” Purpose Anchor reconnects the present effort to a larger purpose or value.
Ex 6: Loss of Identity
Hardship causes you to lose sight of who you are or what you stand for. Purpose Anchor restores stability by reconnecting you with your chosen values, responsibilities, and sense of self.
Ex 7: Apathy Toward the Future
You become indifferent toward goals, consequences, or long-term outcomes. Purpose Anchor identifies a near-term reason to keep moving, restoring momentum one step at a time.
Cures Despair for one ally.""")

autonomy_reclamation = AilmentRecoverySkills("Autonomy Reclamation","Ailment Recovery", 12, 
"""    - Restore independent judgement by re-establishing the boundary between your own thoughts and externally imposed influence. Autonomy Reclamation interrupts frame hijacking, excessive compliance, and identity suppression by consciously examining whether your current beliefs, emotions, decisions, or behaviors genuinely originate from you. Rather than automatically accepting external direction, this skill reactivates critical thought and self-authorship. Brainwash dissolves as borrowed narratives, emotional dependencies, and imposed frames are separated from personally verified beliefs and values, allowing mental sovereignty and independent agency to return.
Trigger cue:
Look slightly upward, gently tap your temple with two fingers, and take a slow inhale. The movement acts as a conditioned cue that immediately brings awareness to the presence of Brainwash, interrupting automatic agreement, emotional synchronization, and externally driven thinking patterns. The temple tap symbolizes the deliberate reactivation of independent thought, while the inhale creates a brief pause between influence and response. This moment of separation allows you to step outside the imposed frame and consciously evaluate it rather than unconsciously following it.
After the cue, deliberately reassess the thought, belief, or impulse by identifying where it came from, whether it aligns with your personal values and experiences, and whether you would still hold the same position without external pressure, validation, authority, or fear of exclusion. By distinguishing personal convictions from inherited or imposed ones, independent judgement and self-directed agency gradually return.
Ex 1: Excessive Agreement
You find yourself agreeing with someone simply because they are charismatic, confident, or high status. Autonomy Reclamation separates their influence from your own genuine beliefs and allows independent evaluation to return.
Ex 2: Authority Bias
You automatically assume that a person, group, or institution must be correct because of their perceived authority. Autonomy Reclamation restores critical thinking by evaluating the claim itself rather than the status of its source.
Ex 3: Group Conformity
You suppress disagreement because you fear standing out or being excluded from the group. Autonomy Reclamation distinguishes social pressure from personal conviction and restores the ability to think independently.
Ex 4: Emotional Dependency
You begin relying excessively on another person’s approval, guidance, or validation when making decisions. Autonomy Reclamation re-establishes trust in your own judgement and personal agency.
Ex 5: Mirroring Behavior
You unconsciously begin adopting another person’s speech patterns, opinions, preferences, or emotional tone. Autonomy Reclamation restores awareness of where the behavior originated and reconnects you with your authentic self.
Ex 6: Ideological Pressure
You begin accepting a narrative or worldview without questioning it because repeated exposure makes it feel unquestionably true. Autonomy Reclamation separates repetition and familiarity from genuine evidence and personal verification.
Ex 7: Identity Suppression
You notice yourself muting your opinions, preferences, or boundaries in order to maintain alignment with someone else’s expectations. Autonomy Reclamation restores awareness of your own values and reasserts your right to independent thought and self-expression.
Cures Brainwash for one ally.""")

attention_snap = AilmentRecoverySkills("Attention Snap","Ailment Recovery", 12, 
"""    - Restore wakefulness and presence by deliberately re-engaging with the current moment through sensory awareness and intentional attention. Attention Snap interrupts zoning out, passive autopilot, mental fog, and emotional disengagement by consciously bringing awareness back to your surroundings and current objective. Rather than forcing alertness through pressure, it reactivates participation by reminding yourself that you are here, now, and capable of choosing where your attention goes. Sleep breaks through self-directed reawakening and renewed presence.
Trigger cue:
 Look at one of your fingers while touching your nose and take a deep inhale at the same time. The combined use of sight, touch, and breath acts as a conditioned cue that immediately brings awareness back into the present moment. By engaging multiple senses at once, mental autopilot is interrupted and attention is pulled away from drifting thoughts, daydreaming, or passive disengagement. After the breath, consciously redirect your attention toward what is happening right now and recommit to active participation.
Ex 1: Zoning Out
 You suddenly realize that you’ve been mentally absent for several minutes. Attention Snap restores awareness by acknowledging that you drifted and intentionally bringing your attention back to the present.
Ex 2: Passive Listening
 Someone has been talking, but you’ve only been nodding without truly processing what they are saying. Attention Snap re-engages your listening and encourages active participation in the conversation.
Ex 3: Mental Fog
 Fatigue causes your thinking to become slow and unfocused. Attention Snap uses sensory grounding to cut through the fog and re-establish awareness of your surroundings and current objective.
Ex 4: Autopilot Behavior
 You are going through actions mechanically without consciously engaging with them. Attention Snap interrupts the automatic behavior and restores deliberate attention and choice.
Ex 5: Daydreaming
 Your thoughts keep wandering away from the task or interaction in front of you. Attention Snap redirects attention away from internal distractions and back toward the present moment.
Ex 6: Emotional Withdrawal
 Stress or discomfort causes you to mentally check out of a situation. Attention Snap gently brings awareness back and encourages re-entry into the interaction rather than continued disengagement.
Ex 7: Study Fatigue
 You’ve been reading or working for a while and realize you haven’t retained anything. Attention Snap restores active attention by re-establishing awareness of the material and your current goal.
Cures Sleep for one ally.""")

recall_thread = AilmentRecoverySkills("Recall Thread","Ailment Recovery", 12, 
"""    - Cure Forget by reconstructing the lost mental thread and restoring access to stalled thoughts, skills, and intentions. Recall Thread stabilizes pressure-induced cognitive disruption by interrupting mental scrambling and returning attention to the last clearly remembered anchor point, whether it be a prior thought, goal, topic, or action. Rather than forcing complete recall, the skill rebuilds momentum one piece at a time, allowing conversational flow, task execution, and Persona skills to resume naturally. Forget fades as access to the missing mental sequence is gradually restored and cognitive flow returns.
Trigger cue:
Pinch your index finger and thumb together while taking a slow breath. The gesture acts as a conditioned cue that immediately brings awareness to the presence of Forget, interrupting panic, mental scrambling, and the urge to force an answer. The pinch symbolizes grasping the lost mental thread before it slips away and creates a brief moment of mental separation from the pressure causing the blank. After the cue, mentally step back and ask yourself what you were just doing, what you were just thinking about, or what your intention was a moment ago. Instead of trying to remember everything at once, return to the last clear point and continue one step at a time. By rebuilding the chain from the last known anchor point, access to stalled thoughts, skills, and actions gradually returns.
Ex 1: Losing Your Train of Thought
You suddenly forget what you were saying mid-conversation. Recall Thread returns to the last sentence or idea you clearly remember and rebuilds the next point from there.
Ex 2: Approach Anxiety
You prepared what to say beforehand but completely blank when the moment arrives. Recall Thread reconnects you with your original intention, allowing you to restart from the first step instead of recalling the entire script.
Ex 3: Presentation Choke
You forget your next point while speaking in front of others. Recall Thread returns to the previous point and allows the next idea to naturally reconnect.
Ex 4: Skill Lock
You know how to perform a social skill or strategy but suddenly cannot access it under pressure. Recall Thread focuses on the last successful action and resumes momentum from there.
Ex 5: Mental Overload
Too much information causes cognitive choking and reduced mental access. Recall Thread strips away unnecessary inputs and reconnects you to your immediate objective.
Ex 6: Interrupted Flow
An unexpected interruption causes you to lose your momentum and forget what you were doing. Recall Thread retraces the last clear action and rebuilds the sequence from there.
Ex 7: High-Stakes Pressure
The importance of the moment causes your mind to freeze despite knowing what you want to do. Recall Thread reduces the pressure to remember everything and instead focuses on recovering only the next step.
Cures Forget for one ally.""")


singular_ailment_recovery_skills = (frame_reset, hazard_audit, temper_drop, purpose_anchor,
                                    autonomy_reclamation, attention_snap, recall_thread)
aoe_ailment_recovery_sklils = ()
all_ailment_recovery_skills = ()
