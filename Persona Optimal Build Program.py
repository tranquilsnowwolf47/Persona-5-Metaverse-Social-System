
# Filename: Persona Optimal Build Program.py
# Date: 1/30/25
# Author: Aoi | shadowsnowwolf

# A program meant to display the optimal build template of each Arcana 
# Program idea: 
# Persona build randomizer 
# uses random.choice from an array
# New realization: You can use F strings in function parameters

list_of_arcanas = ("Fool","Magician","Priestes","Empress","Emperor","Hierophant",
                   "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                    "Hanged Man","Death","Temperance","Devil","Tower","Star",
                    "Moon","Sun","Judgement","Faith","Councillor") # A tuple that will hold the list of all valid Arcanas

#print(len(list_of_arcanas)) # Debugging


def display_fool_optimal_build(arcana=f"{list_of_arcanas[0]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("Any 8 skills of your choice ")
display_fool_optimal_build() 

def display_magician_optimal_build(arcana=f"{list_of_arcanas[1]}", **kwargs,): # using kwargs for the element + number
    print(f"{arcana} Persona Optimal Build Template:")
    print("skills")
    print(kwargs)

display_magician_optimal_build(wind=8)

def display_optimal_build(arcana=f"{list_of_arcanas[2]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")
       
def display_optimal_build(arcana=f"{list_of_arcanas[3]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[4]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[5]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[6]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[7]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[8]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[9]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[10]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[11]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[12]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[13]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[14]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[15]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[16]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[17]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[18]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[19]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")
def display_optimal_build(arcana=f"{list_of_arcanas[20]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[21]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=f"{list_of_arcanas[22]}"):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")
def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

def display_optimal_build(arcana=""):
    print(f"{arcana} Persona Optimal Build Template:")
    print("")

is_valid_arcana_choice = False
try:
    arcana_choice = input("Please enter an Arcana: ") # Get the user input
    if arcana_choice in list_of_arcanas: # validate the input 
        is_valid_arcana_choice = True
        if arcana_choice == list_of_arcanas[0]:
            pass 
        elif arcana_choice == list_of_arcanas[1]:
            pass
        elif arcana_choice == list_of_arcanas[2]:
            pass
        elif arcana_choice == list_of_arcanas[3]:
            pass
        elif arcana_choice == list_of_arcanas[4]:
            pass
        elif arcana_choice == list_of_arcanas[5]:
            pass
        elif arcana_choice == list_of_arcanas[6]:
            pass
        elif arcana_choice == list_of_arcanas[7]:
            pass
        elif arcana_choice == list_of_arcanas[8]:
            pass
        elif arcana_choice == list_of_arcanas[9]:
            pass
        elif arcana_choice == list_of_arcanas[10]:
            pass
        elif arcana_choice == list_of_arcanas[11]:
            pass
        elif arcana_choice == list_of_arcanas[12]:
            pass
        elif arcana_choice == list_of_arcanas[13]:
            pass
        elif arcana_choice == list_of_arcanas[14]:
            pass
        elif arcana_choice == list_of_arcanas[15]:
            pass
        elif arcana_choice == list_of_arcanas[16]:
            pass
        elif arcana_choice == list_of_arcanas[17]:
            pass
        elif arcana_choice == list_of_arcanas[18]:
            pass
        elif arcana_choice == list_of_arcanas[19]:
            pass
        elif arcana_choice == list_of_arcanas[20]:
            pass
        elif arcana_choice == list_of_arcanas[21]:
            pass
        elif arcana_choice == list_of_arcanas[22]:
            pass
except:
    raise ValueError("Incorrect Arcana entered")
