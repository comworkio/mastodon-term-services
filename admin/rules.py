import os
import yaml
from utils.db import sql_exec, sql_exec_values
from utils.logger import log_msg

sql = "INSERT INTO rules (created_at, updated_at, text, priority) VALUES (NOW(), NOW(), %s, %s)"

with open(os.environ['CONFIG_FILE'], "r") as stream:
    config = yaml.safe_load(stream)
    sql_exec("DELETE FROM rules")
    for rule in config['rules']:
        log_msg("INFO", "Inserting this rule: {}".format(rule['text']))
        sql_exec_values(sql, (rule['text'], rule['priority'],))
