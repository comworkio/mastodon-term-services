from utils.file import file_get_contents
from utils.db import sql_execute

import os

sql = "UPDATE settings SET updated_at = NOW(), value = %s WHERE var = 'site_terms'"

sql_execute(sql, file_get_contents(os.environ['TERMS_FILE_PATH']))
