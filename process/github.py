from github import Github


class GithubAdapter:

    def __init__(self, username: str, password: str, organization: str):
        self.github = Github(username, password)
        self.organization = self.github.get_organization(organization)

    def download(self, repo, target):
        pass
