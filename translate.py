from asyncio import sleep
import random
from deep_translator import GoogleTranslator

def format_string(input_str):
    if "-" not in input_str:
        return "Formato non valido: usa 'chiave - testo_italiano'"
    
    parts = input_str.split("-", 1)
    key = parts[0].strip().lower().replace(" ", "_")
    italian_text = parts[1].strip()

    try:
        
        sleep(random.uniform(1, 3))
        translated = GoogleTranslator(source='it', target='en').translate(italian_text)
        return f'<string name="{key}">{italian_text}</string>\n<string name="{key}">{translated}</string>'
    except Exception as e:
        return f"Errore di traduzione: {str(e)}"

if __name__ == "__main__":
    print("Inserisci testo in formato 'chiave - testo_italiano' (scrivi 'exit' per uscire):")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":
            print("Programma terminato.")
            break
        print(format_string(user_input))