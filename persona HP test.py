def calculateHP(HP_PER_LEVEL,current_user_level):
    return HP_PER_LEVEL * current_user_level
    


def displayNewHPTotal():
    calculation = calculateHP(10,12)
    print(f"HP: {calculation}")
    print(f"SP: {calculation}")

displayNewHPTotal()