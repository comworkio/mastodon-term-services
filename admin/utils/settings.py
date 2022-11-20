import os

from utils.db import sql_exec_value
from utils.logger import log_msg

def update_settings(db_key, env_var_key, format_function):
    sql = "UPDATE settings SET updated_at = NOW(), value = %s WHERE var = '{}'".format(db_key)
    log_msg("INFO", "Updating {}".format(db_key))
    sql_exec_value(sql, format_function(os.environ[env_var_key]))
