from core.folders_init import FOLDER_HISTORY
from datetime import datetime, timezone

def _cleanup_old_logs() -> None:
    cutoff_140 = datetime.now(timezone.utc).timestamp() - (140 * 86400)
    for f in FOLDER_HISTORY.glob("graphmaker_*.jsonl"):
        if f.stat().st_mtime < cutoff_140:
            f.unlink()

    files = sorted(
        FOLDER_HISTORY.glob("graphmaker_*.jsonl"),
        key=lambda x: x.stat().st_mtime
    )
    
    if len(files) > 90:
        files_to_delete = files[:-90]
        for f in files_to_delete:
            f.unlink()