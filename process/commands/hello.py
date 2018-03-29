from ..utils import timed
from .base_cmd import Command

import logging
import time

logger = logging.getLogger(__name__)


@timed
def hello():
    time.sleep(0.5)


class HelloActivity(Command):

    fields = []

    def execute(self):
        hello()
