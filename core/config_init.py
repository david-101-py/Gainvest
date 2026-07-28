import json
from core.files_init import CONFIG_FILE
def load_config():
    '''Necesita que se haya cargado bootstrap en main sí o sí'''
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)
    return config