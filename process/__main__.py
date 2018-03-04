import os, sys

sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    logging.info(dict(message='hello world'))
