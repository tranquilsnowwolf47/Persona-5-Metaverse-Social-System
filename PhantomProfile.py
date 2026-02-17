# use encapsulation 
# Maybe I'll private the attributes 
class PhantomProfile:
    def __init__(self, name, phantom_level, arcana, main_persona,
                 main_elemental_affinity, 
                 base_HP, base_SP,
                 base_st, base_ma, base_en, base_ag, base_lu,
                 phys_affinity, reverse_phys_affinity,
                 gun_affinity, reverse_gun_affinity,
                 fire_affinity, reverse_fire_affinity,
                 ice_affinity, reverse_ice_affinity,
                 elec_affinity, reverse_elec_affinity,
                 wind_affinity, reverse_wind_affinity,
                 psy_affinity, reverse_psy_affinity,
                 nuke_affinity, reverse_nuke_affinity,
                 bless_affinity, reverse_bless_affinity,
                 curse_affinity, reverse_curse_affinity):
        
        # General info
        self.name = name
        self.phantom_level = phantom_level
        self.arcana = arcana
        self.main_persona = main_persona
        self.main_elemental_affinity = main_elemental_affinity
    
        # Combat stats
        # HP and SP
        self.base_HP = base_HP
        self.base_SP = base_SP

        # Battle stats 
        self.base_st = base_st # Base Strength stat
        self.base_ma = base_ma # Base Magic stat
        self.base_en = base_en # Base Endurance stat 
        self.base_ag = base_ag # Base Agility stat
        self.base_lu = base_lu # Base Luck stat

        # Elemental affinities
        # Phys affinities
        self.phys_affnity = phys_affinity
        self.reverse_phys_affinity = reverse_phys_affinity
        
        # Gun affinities
        self.gun_affinity = gun_affinity
        self.reverse_gun_affinity = reverse_gun_affinity
        
        # Fire affinities
        self.fire_affinity = fire_affinity
        self.reverse_fire_affinity = reverse_fire_affinity
        
        # Ice affinities
        self.ice_affinity = ice_affinity
        self.reverse_ice_affinity = reverse_ice_affinity
        
        # Elec affinities
        self.elec_affinity = elec_affinity
        self.reverse_elec_affinity = reverse_elec_affinity
        
        # Wind affinities
        self.wind_affinity = wind_affinity
        self.reverse_wind_affinity = reverse_wind_affinity
        
        # Psy affinities
        self.psy_affinity = psy_affinity
        self.reverse_psy_affinity = reverse_psy_affinity

        # Nuke affinities
        self.nuke_affinity = nuke_affinity
        self.reverse_nuke_affinitiy = reverse_nuke_affinity

        # Bless affinities
        self.bless_affinity = bless_affinity
        self.reverse_bless_affinity = reverse_bless_affinity

        # Curse affinities
        self.curse_affinity = curse_affinity
        self.reverse_curse_affinity = reverse_curse_affinity

    # Function that adds a level to the base Phantom Level 
    def level_up(self,):
        self.phantom_level += 1

    # Function that displays info of the user's Phantom Profile 
    def display_phantom_profile(self):
        print("Phantom Profile:")
        print("-----------------------------------------")
        print(f"Name: {self.name}")
        print(f"Phantom Level: {self.phantom_level}")
        print(f"Arcana: {self.arcana}")
        print(f"Main Persona: {self.main_persona}")
        print(f"Main Elemental Affinity: {self.main_elemental_affinity}")
        print(f"Base HP: {self.base_HP}")
        print(f"Base SP: {self.base_SP}")
        print(f"St: {self.base_st}")
        print(f"Ma: {self.base_ma}")
        print(f"En: {self.base_en}")
        print(f"Ag: {self.base_ag}")
        print(f"Lu: {self.base_lu}")

    # Function that displays the elemental affinities of the user 
    def display_elemental_affinities(self):
        print("\n\nElemental Affinities: ")
        print("-----------------------------------------")
        print(f"Phys: {self.phys_affnity}   | Rev. Phys: {self.phys_affnity}")
        print(f"Gun: {self.gun_affinity}   | Rev. Gun: {self.gun_affinity}")
        print(f"Fire: {self.fire_affinity} | Rev. Fire: {self.reverse_fire_affinity}")
        print(f"Ice: {self.ice_affinity}   | Rev. Ice: {self.reverse_ice_affinity}")
        print(f"Elec: {self.elec_affinity}   | Rev. Elec: {self.reverse_elec_affinity}")
        print(f"Wind: {self.wind_affinity}   | Rev. Wind: {self.reverse_wind_affinity}")
        print(f"Psy: {self.psy_affinity}     | Rev. Psy: {self.reverse_psy_affinity}")
        print(f"Nuke: {self.nuke_affinity}   | Rev. Nuke: {self.reverse_nuke_affinitiy}")
        print(f"Bless: {self.bless_affinity}   | Rev. Bless: {self.reverse_bless_affinity}")
        print(f"Curse: {self.curse_affinity}   | Rev. Curse: {self.reverse_curse_affinity}")
        #print(f"X: {self.affinity}")

# Affinitiy abbreviations
weak_affinity = "Wk" 
neutral_affinity = "Neutral"
resist_affinity = "Str"
null_affinity = "Nul"
drain_affinity = "Dr"
repel_affinity = "Rpl" 

aoi = PhantomProfile("Aoi", 41, "Fool", "Arsene", "Curse", 260, 260, 0, 0, 0, 0, 0, 
weak_affinity, weak_affinity, # phys
weak_affinity, weak_affinity, # gun
resist_affinity, resist_affinity, # fire
resist_affinity, weak_affinity, # ice
neutral_affinity, resist_affinity, # elec
neutral_affinity, resist_affinity, # wind
resist_affinity, resist_affinity, # psy
neutral_affinity, neutral_affinity, # nuke
weak_affinity, neutral_affinity, # bless
neutral_affinity, resist_affinity) # curse

for i in range(3):
    aoi.level_up()

aoi.display_phantom_profile()
aoi.display_elemental_affinities()
#aoi.level_up()



