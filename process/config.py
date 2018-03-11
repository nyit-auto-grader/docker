from configparser import ConfigParser
from pathlib import Path
import os

config_file = Path(__file__).parents[1] / 'local' / 'config.ini'
config_parser = ConfigParser()
if config_file.exists():
    config_parser.read(config_file)


class Config:
    teacher = dict(username=None, token=None)
    organization = None

    def __getitem__(self, item):
        return getattr(self, item)


class DevConfig(Config):
    teacher = dict(
        username=os.environ.get('TEACHER'),
        token=os.environ.get('TOKEN')
    )
    organization = os.environ.get('ORGANIZATION')


class ProdConfig(DevConfig):
    pass


class TestConfig(Config):
    teacher = dict(
        username=config_parser['github']['username'],
        token=config_parser['github']['token'],
    )
    organization = config_parser['github']['organization']


configs = dict(dev=DevConfig, prod=ProdConfig, test=TestConfig)


def build_config(mode: str='dev'):
    return configs[mode]()
