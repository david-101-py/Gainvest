import json
from pathlib import Path
from core.files_init import CONFIG_FILE

def load_config():
    '''Necesita que se haya cargado bootstrap en main sí o sí'''
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)
    return config

def update_config(new_config_data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        if isinstance(new_config_data, dict):
            json.dump(new_config_data, file, indent=4)
        else:
            file.write(str(new_config_data))

def show_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)
        config_dict = config.get("config", {})
        keys = list(config_dict.keys())
        
        print("Configuration file content:")
        for i, (key, value) in enumerate(config_dict.items(), 1):
            print(f"{i}: {key} ({value})")
    return config, keys
    

def modify_config():
    config, keys = show_config()
    try:
        op = int(input("¿Qué quieres modificar? (número): "))
        if op < 1 or op > len(keys):
            print("Número fuera de rango.")
            return
        key = keys[op - 1]
        current_val = config["config"][key]
        new_val = input(f"Nuevo valor para '{key}' (actual: {current_val}): ")
        if isinstance(current_val, bool):
            new_val = new_val.lower() in ("true", "1", "sí", "si", "yes")
        elif isinstance(current_val, int):
            new_val = int(new_val)
        elif isinstance(current_val, float):
            new_val = float(new_val)
        config["config"][key] = new_val
        update_config(config)
        print("Configuración actualizada.")
    except (ValueError, IndexError):
        print("Entrada inválida.")
    

