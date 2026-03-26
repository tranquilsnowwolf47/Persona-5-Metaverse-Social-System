import PersonaEXPProgram

kaguya = PersonaEXPProgram.Persona("Kaguya","Moon",35,1,12,8,13,5,0)
barong = PersonaEXPProgram.Persona("Barong","Emperor","35",15,11,7,5,1,0)
#barong.display_persona_info()
#barong.level_up()
#barong.display_persona_info
izanagi = PersonaEXPProgram.Persona("Izanagi","Fool",35,8,8,6,8,9,0)

barong.display_persona_info()
print()
barong.allot_st()
barong.allot_ma()
barong.allot_en()
barong.allot_ag()
barong.allot_lu()
print()
barong.display_persona_info()
