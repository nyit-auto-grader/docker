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
    askpass = Path(__file__).parents[1] / 'askpass.py'
    git = dict(trace=None, target=None)

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return dict(teacher=self.teacher, organization=self.organization, askpass=self.askpass, git=self.git)

    @property
    def github_params(self):
        return dict(username=self.teacher['username'], password=self.teacher['token'], organization=self.organization,
                    askpass=self.askpass, git_trace=self.git['trace'], git_target=self.git['target'])


class DevConfig(Config):
    teacher = dict(
        username=os.environ.get('TEACHER'),
        token=os.environ.get('TOKEN')
    )
    organization = os.environ.get('ORGANIZATION')
    git = dict(trace='1', target='/usr/local/bin/git')


class ProdConfig(DevConfig):
    pass


class TestConfig(Config):
    teacher = dict(
        username=config_parser['github']['username'],
        token=config_parser['github']['token'],
    )
    organization = config_parser['github']['organization']
    git = dict(trace='full', target='/usr/local/bin/git')


configs = dict(dev=DevConfig, prod=ProdConfig, test=TestConfig)


def build_config(mode: str=None):
    return configs[mode or 'dev']()
