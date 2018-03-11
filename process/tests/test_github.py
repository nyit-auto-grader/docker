from ..github import GithubAdapter
from ..config import build_config
import unittest


class GithubAdapterTester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = build_config('test')

    def test_tdd(self):
        params = self.config.teacher['username'], self.config.teacher['token'], self.config.organization
        dut = GithubAdapter(*params)
        print(dut)

