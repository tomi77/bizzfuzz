import sys
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'bizzfuzz.settings'

import django
from django.test.utils import get_runner
from django.conf import settings


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    if hasattr(django, 'setup'):
        django.setup()
    failures = test_runner.run_tests(['accounts'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
