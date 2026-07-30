from core.folders_init import HIDDEN_BASE_DIR
from core.files_init import CONFIG_FILE
from core.db_core import _create_sql_tables
from core.history_init import _cleanup_old_logs

_cleanup_old_logs()
_create_sql_tables()