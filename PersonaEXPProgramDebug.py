# Debug program for the Persona EXP Program




import PersonaEXPProgram
izanagi_picaro = PersonaEXPProgram.Persona("Izanagi Picaro","Fool",31,9,7,1,8,9,1)
sandman = PersonaEXPProgram.Persona("Sandman","Magician",)
anubis = PersonaEXPProgram.Persona("Anubis","Judgement",)
berith = PersonaEXPProgram.Persona("Berith","Hierophant",)
genbu = PersonaEXPProgram.Persona("Genbu","Temperance",)
orlov = PersonaEXPProgram.Persona("Orlov","Strength",)
sudama = PersonaEXPProgram.Persona("Sudama","Hermit",)
lamia = PersonaEXPProgram.Persona("Lamia","Empress",)
okuninushi = PersonaEXPProgram.Persona("Okuninushi","Faith",)
narcissus = PersonaEXPProgram.Persona("Narcissus","Lovers",)
belphegor = PersonaEXPProgram.Persona("Belphegor","Tower",)
hell_biker = PersonaEXPProgram.Persona("Hell Biker","Death",)

# Performs operations for all personas in the tuple
personas = (izanagi_picaro, sandman, anubis, berith, genbu, orlov, sudama, lamia, okuninushi, narcissus, belphegor, hell_biker)
for persona in personas:
    PersonaEXPProgram.Persona.display_menu(persona)

#lachesis.display_persona_info()
#lachesis.level_up()
#lachesis.display_persona_info()
#print()
#lachesis.allot_st()
#lachesis.allot_ma()
#lachesis.allot_en()
#lachesis.allot_ag()
#lachesis.allot_lu()
#print()
#lachesis.display_persona_info()


#PersonaEXPProgram.Persona.display_menu(izanagi)

