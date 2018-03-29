from ..adapters import GithubAdapter
from .base_cmd import Command

from pathlib import Path
import logging

logger = logging.getLogger(__name__)
temp_dir = Path(__file__).parents[1] / 'tests' / 'temp'


class GradeActivity(Command):
    fields = ['teacher', 'organization', 'askpass', 'git', 'repo']

    @property
    def github_params(self):
        return dict(
            username=self.teacher['username'],
            password=self.teacher['token'],
            organization=self.organization,
            askpass=self.askpass,
            git_trace=self.git['trace'],
            git_target=self.git['target']
        )

    def setup(self):
        self.github = GithubAdapter(**self.github_params)

    def execute(self):
        logger.info(None, extra=dict(activity='grade'))
        logger.info(None, extra=dict(temp_dir=temp_dir))
        print(self.github)
        print(self.repo)
