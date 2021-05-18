T = int(input(""))
for i in range (T):
    sheldon, raj = input("").split()
    
    if sheldon == raj:
        result = "De novo!"
        
    elif sheldon == "tesoura":
        if raj == "papel" or raj == "lagarto":
            result = sheldon
        else:
            result = raj
            
    elif sheldon == "papel":
        if raj == "pedra" or raj == "Spock":
            result = sheldon
        else:
            result = raj
    
    elif sheldon == "pedra":
        if raj == "lagarto" or raj == "tesoura":
            result = sheldon
        else:
            result = raj
    
    elif sheldon == "lagarto":
        if raj == "Spock" or raj == "papel":
            result = sheldon
        else:
            result = raj
    
    elif sheldon == "Spock":
        if raj == "tesoura" or raj == "pedra":
            result = sheldon
        else:
            result = raj
        
    if result == sheldon:
        result = "Bazinga!"
    elif result == raj:
        result = "Raj trapaceou!"
    
    print(f"Caso #{i+1}: {result}")