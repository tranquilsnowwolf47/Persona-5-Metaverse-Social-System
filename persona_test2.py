def fusePersona():
    personas = []
    for x in range(2):
        fusionChoice = input("Please enter a Persona: ")
        personas.append(fusionChoice)
    return personas


result = fusePersona()
print(result)