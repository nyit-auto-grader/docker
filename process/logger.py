from pythonjsonlogger import jsonlogger
from datetime import datetime
from typing import List
import logging


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        now = datetime.utcnow()
        if not log_record.get('date'):
            log_record['date'] = now.strftime('%Y-%m-%d')
        if not log_record.get('time'):
            log_record['time'] = now.strftime('%H:%M:%S')
        if log_record.get('level'):
            log_record['level'] = log_record['level'].lower()
        else:
            log_record['level'] = record.levelname.lower()
        for field in ['module', 'lineno']:
            log_record[field] = getattr(record, field)
        log_record['function'] = record.funcName
        for field in ['exc_info', 'exc_text']:
            value = getattr(record, field)
            if value:
                log_record[field] = value


class LoggerFactory:
    @staticmethod
    def build(name: str, level_name: str='info', fields: List[str]=None):
        if fields is None:
            fields = ['date', 'time', 'level', 'module', 'function', 'lineno', 'name', 'message']
        logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        fields_joined = ' '.join(f'({field})' for field in fields)
        formatter = CustomJsonFormatter(fields_joined)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        level = logging._nameToLevel[level_name.upper()]
        logger.setLevel(level)
        return logger
