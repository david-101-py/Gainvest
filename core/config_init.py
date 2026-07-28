import json
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