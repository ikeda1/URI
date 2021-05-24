for i in range(int(input())):
    sheldon, raj  = input().split()
    
    dict = {"pedra": ["tesoura", "lagarto"],
            "papel": ["pedra", "Spock"],
            "tesoura": ["papel", "lagarto"],
            "lagarto": ["Spock", "papel"],
            "Spock": ["tesoura", "pedra"]}
    if raj in dict[sheldon]:
        win = sheldon
    else:
        win = raj
    
    if raj == sheldon:
        win = "De novo!"
    elif win == sheldon:
        win = "Bazinga!"
    elif win == raj:
        win = "Raj trapaceou!"
    print(f"Caso #{i+1}: {win}")
    