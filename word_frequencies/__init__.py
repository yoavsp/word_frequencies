import logging
import logging.config
from os import path

log_setting_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_setting_file_path)