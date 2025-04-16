import os
from time import sleep
import random
from deep_translator import GoogleTranslator

# Dizionario per evitare duplicati
translations_dict = {
    'android': {},
    'ios': {}
}

def format_string(input_str, system_type):
    if "-" not in input_str:
        return "\n❌ Formato non valido. Usa: 'chiave - testo_italiano'\n"
    
    parts = input_str.split("-", 1)
    key = parts[0].strip().lower().replace(" ", "_")
    italian_text = parts[1].strip()

    # Controllo duplicati
    if key in translations_dict[system_type]:
        return f"\n⚠️ Attenzione: la chiave '{key}' esiste già!\n"

    try:
        # Traduzione con timeout progressivo
        max_retries = 3
        for attempt in range(max_retries):
            try:
                sleep(random.uniform(1, 3 * (attempt + 1)))  # Timeout crescente
                translated = GoogleTranslator(source='it', target='en').translate(italian_text)
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"⚠️ Tentativo {attempt + 1} fallito. Riprovo...")

        # Salva la traduzione
        translations_dict[system_type][key] = {
            'it': italian_text,
            'en': translated
        }

        # Formattazione specifica
        if system_type == "android":
            return f'<string name="{key}">{italian_text}</string>\n<string name="{key}_en">{translated}</string>'
        else:
            return f'"{key}" = "{italian_text}";\n"{key}_en" = "{translated}";'

    except Exception as e:
        return f"\n❌ Errore: {str(e)}\n"

def save_to_file(system_type):
    if not translations_dict[system_type]:
        print("\n⚠️ Nessuna traduzione da salvare!")
        return

    filename = f"translations_{system_type}.{'xml' if system_type == 'android' else 'strings'}"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            if system_type == "android":
                f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')
                for key, values in translations_dict[system_type].items():
                    f.write(f'    <string name="{key}">{values["it"]}</string>\n')
                    f.write(f'    <string name="{key}_en">{values["en"]}</string>\n')
                f.write('</resources>')
            else:
                for key, values in translations_dict[system_type].items():
                    f.write(f'"{key}" = "{values["it"]}";\n')
                    f.write(f'"{key}_en" = "{values["en"]}";\n')
        
        print(f"\n✅ File salvato correttamente come: {filename}")
        print(f"📝 Totale traduzioni: {len(translations_dict[system_type])}")
    except Exception as e:
        print(f"\n❌ Errore nel salvataggio: {str(e)}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("TRADUTTORE ANDROID/iOS AVANZATO".center(50))
    print("="*50)

    # Scelta del sistema con controllo input
    system = ""
    while system not in ["android", "ios"]:
        system = input("\nSeleziona sistema (android/ios): ").lower()
        if system in ("exit", "esc", "fine"):
            print("\nArrivederci!")
            exit()

    print(f"\n🔧 Modalità {system.upper()} attivata")
    print("Scrivi 'save' per salvare le traduzioni")
    print("Scrivi 'exit' per uscire\n")

    while True:
        user_input = input(">>> ").strip()
        
        # Comandi speciali
        if user_input.lower() in ("exit", "esc", "fine"):
            if translations_dict[system]:
                save = input("Salvare le traduzioni prima di uscire? (s/n): ").lower()
                if save == 's':
                    save_to_file(system)
            print("\nArrivederci!")
            break
            
        elif user_input.lower() == "save":
            save_to_file(system)
            continue
            
        # Processa la traduzione
        result = format_string(user_input, system)
        print(result)