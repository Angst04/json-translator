import json
import os
from translatepy import Translator
import time

def translate_text(text, translator):
    try:
        time.sleep(0.1)
        return translator.translate(text, destination_language="en").result
    except Exception as e:
        print(f"Ошибка перевода: {str(e)}")
        return text

def translate_dict(data, translator):
    if isinstance(data, dict):
        return {k: translate_dict(v, translator) for k, v in data.items()}
    elif isinstance(data, str):
        return translate_text(data, translator)
    else:
        return data

def main():
    target_dir = "target"
    translated_dir = "translated"
    
    os.makedirs(translated_dir, exist_ok=True)
    
    if not os.path.exists(target_dir):
        print(f"Directory '{target_dir}' not found!")
        return

    translator = Translator()
    
    for filename in os.listdir(target_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(target_dir, filename)
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                translated_data = translate_dict(data, translator)
                
                output_path = os.path.join(translated_dir, filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(translated_data, f, ensure_ascii=False, indent=2)
                
                print(f"Successfully processed: {filename}")
            
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    main()