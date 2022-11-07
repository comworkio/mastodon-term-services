from utils.logger import log_msg
from utils.file import file_get_contents
from utils.db import sql_execute

import os

sql = "UPDATE settings SET updated_at = NOW(), value = %s WHERE var = 'site_terms'"

log_msg("INFO", "Updating term of uses")
sql_execute(sql, file_get_contents(os.environ['TERMS_FILE_PATH']))
