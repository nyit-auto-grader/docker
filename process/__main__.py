import os, sys

sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    from process.logger import LoggerFactory
    import logging

    logger = LoggerFactory.build('process', logging.INFO)
    logger.info('hello world', extra=dict(x=1))

