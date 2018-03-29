from ..adapters import GithubAdapter
from ..config import build_config
from ..utils import rmtree
from pathlib import Path
import unittest
import functools

temp_dir = Path(__file__).parent / 'temp'


def target(path: Path):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(self):
            self.target = path
            if self.target.exists():
                rmtree(self.target)
            self.assertFalse(self.target.exists())
            return fn(self)
        return wrapper
    return decorator


class GithubAdapterTester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = build_config('test')
        cls.target = None

    def setUp(self):
        self.github = GithubAdapter(**self.config.github_params)

    def tearDown(self):
        self.target = None

    @target(temp_dir / 'rkhullar-nyit' / 'project-base')
    def test_git_clone_public_1(self):
        url = 'https://github.com/rkhullar-nyit/project-base.git'
        self.github.download(url, self.target)
        self.assertTrue(self.target.exists())

    @target(temp_dir / 'CSCI125-Spring2018' / 'project03-rkhullar')
    def test_git_clone_private_1(self):
        url = 'https://github.com/CSCI125-Spring2018/project03-rkhullar.git'
        self.github.download(url, self.target)
        self.assertTrue(self.target.exists())

    @target(temp_dir / 'rkhullar' / 'python-snippets')
    def test_git_clone_private_2(self):
        url = 'https://github.com/rkhullar-python-snippets.git'
        self.github.download(url, self.target)
        self.assertFalse(self.target.exists())
