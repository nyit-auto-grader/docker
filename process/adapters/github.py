from github import Github
from git import Repo
from typing import NamedTuple, Union
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class GithubAdapter(NamedTuple):

    username: str
    password: str
    organization: str
    askpass: Path
    git_trace: str = None
    git_target: str = None

    @property
    def github(self) -> Github:
        return Github(self.username, self.password)

    @property
    def github_org(self):
        return self.github.get_organization(self.organization)

    def download(self, repo: str, target: Union[Path, str]):
        env = {'GIT_USERNAME': self.username, 'GIT_PASSWORD': self.password, 'GIT_ASKPASS': str(self.askpass),
               'GIT_PYTHON_TRACE': self.git_trace, 'GIT_PYTHON_GIT_EXECUTABLE': self.git_target}
        try:
            repo = Repo.clone_from(repo, target, env=env)
            repo.submodule_update()
        except Exception:
            logger.exception('could not download', extra=dict(repo=repo))
