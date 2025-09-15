def storePersonas():
    personas = []
    persona_number = 0
    for x in range(2):
        persona_number += 1
        persona_choice = input(f"Please enter a persona: #{persona_number}: ")
        personas.append(persona_choice)

def displayPersonas(personas):
    return personas

    
class PersonaFusion:
    def __init__(self,personas,persona_number):
        self.personas = personas
        self.persona_number = persona_number


    def storePersonas(self):
        self.personas = []
        for x in range(2):
            self.persona_number += 1
            persona_choice = input(f"Please enter a persona: #{self.persona_number}: ")
            self.personas.append(persona_choice)

    def displayPersonas():
        return self.personas
    

p1 = PersonaFusion("",1)
