from pathlib import Path
import datetime
from core.config_init import load_config
from core.folders_init import visible_folders

def return_file_age(file_path):
    if file_path.exists():
        date = datetime.datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%d/%m/%Y %H:%M')
        return date
    return None

def clear_exports():
    config_data = load_config()
    max_live_time = config_data["config"]["export_lifetime"]
    for folder in ["GRAPH_DIR", "TABLE_DIR", "HTML_GRAPH_DIR"]:
        path = visible_folders[folder]
        ages = {}
        for file in path.iterdir():
            if file.is_file():
                ages[file.name] = return_file_age(file)
    for file in ages:
        file_path = path / file
        if datetime.datetime.now() - datetime.datetime.strptime(ages[file], '%d/%m/%Y %H:%M') > datetime.timedelta(days=max_live_time):
            file_path.unlink()
    print(f"Deleted files older than {max_live_time} days.")


        