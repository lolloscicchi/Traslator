import json
from langdetect import detect
from googletrans import Translator

# Funzione per tradurre il testo in inglese
def translate_text(text, target_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

# Funzione per processare il JSON
def process_json(input_json):
    output_json = {}
    
    for key, value in input_json.items():
        try:
            # Rileviamo la lingua del valore
            language = detect(value)
            if language == 'it':  # Se il testo è in italiano
                translated_value = translate_text(value)
                output_json[key] = translated_value
            else:
                output_json[key] = value
        except Exception as e:
            output_json[key] = value  # In caso di errore lasciamo il valore originale
    
    return output_json

# Funzione per leggere il file di input e scrivere il file di output
def process_file(input_file, output_file):
    # Leggiamo il file di input JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        input_json = json.load(f)
    
    # Elaboriamo i dati
    output_json = process_json(input_json)
    
    # Scriviamo il file di output JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_json, f, indent=4, ensure_ascii=False)

# Eseguiamo la funzione su file specifici
input_file = 'input.json'  # Nome del file di input
output_file = 'output.json'  # Nome del file di output

process_file(input_file, output_file)

print(f"File di output creato: {output_file}")
