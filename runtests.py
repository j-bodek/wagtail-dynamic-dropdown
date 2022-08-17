import argparse
import os
import sys

from django.core.management import execute_from_command_line

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


def runtests():
    args, rest = argparse.ArgumentParser().parse_known_args()

    argv = [sys.argv[0], "test"] + rest
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()