import logging
import re
from logging.handlers import TimedRotatingFileHandler
import os

config = [
    {
        'name': None,
        'file_name': 'flask.log',
        'level': logging.INFO
    }
]

def log_init():
    log_fmt = '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(log_fmt)
    logging.basicConfig(level=logging.INFO, format=log_fmt, )

    for c in config:
        t = os.path.split(c["file_name"])
        log_path = 'logs/' + t[0]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        handler = TimedRotatingFileHandler(filename=f'logs/{c["file_name"]}', when="MIDNIGHT", interval=1, backupCount=7)
        handler.suffix = "%Y-%m-%d_%H-%M.log"
        handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
        handler.setFormatter(formatter)
        handler.setLevel(c['level'])
        logging.getLogger(c['name']).addHandler(handler)
