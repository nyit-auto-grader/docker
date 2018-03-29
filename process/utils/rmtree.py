from pathlib import Path


def rmtree(p: Path):
    """
    recursively delete directory contents

    p = Path('/path/to/folder')
    rmtree(p)

    """

    for q in p.iterdir():
        if q.is_dir():
            rmtree(q)
        else:
            q.unlink()
    p.rmdir()
