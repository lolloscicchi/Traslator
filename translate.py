def format_string(input_str):
    if "-" not in input_str:
        return "Formato non valido: usa 'stringa1 - stringa2'"
    
    parts = input_str.split("-", 1)
    
    # Elabora la prima parte: lowercase + sostituisci spazi con _
    part1 = parts[0].strip().lower().replace(" ", "_")
    part2 = parts[1].strip()  # Lascia la seconda parte invariata
    
    return f'<string name="{part1}">{part2}</string>'

def main():
    print("Inserisci due stringhe separate da '-' (scrivi 'esc' per uscire)")
    while True:
        user_input = input(">>> ")
        
        if user_input.lower() == "esc":
            print("Uscita dal programma.")
            break
        
        output = format_string(user_input)
        print(output)

if __name__ == "__main__":
    main()