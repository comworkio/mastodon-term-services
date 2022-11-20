import os

from utils.file import config_settings
from utils.db import sql_exec_value
from utils.logger import log_msg

def update_settings(db_key, env_var_key):
    sql = "UPDATE settings SET updated_at = NOW(), value = %s WHERE var = '{}'".format(db_key)
    log_msg("INFO", "Updating {}".format(db_key))
    sql_exec_value(sql, config_settings(os.environ[env_var_key]))
