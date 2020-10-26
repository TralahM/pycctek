#!/usr/bin/env python
"""Data Loader Module.

Utilities to load Bank Indentification Numbers, more recently referred to as
Issuer Identification Numbers from the YAML format into python Objects.
"""
from yaml import load  # ,dump

# from pprint import pprint
import json
import os

try:
    from yaml import CLoader as Loader  # ,CDumper as Dumper
except ImportError:
    from yaml import Loader  # ,Dumper


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class InvalidIIN(Exception):
    """Exception Handler for Too Short IIN|BIN Inputs."""

    pass


def build_iin_path(iin):
    """Return the Appropriate Path to the specified IIN|BIN."""
    if isinstance(iin, int):
        iin = str(iin)
    if not len(iin) >= 4:
        raise InvalidIIN("Issuer Identification Number Too Short < 6")
    return os.path.join(CURRENT_DIR, f"data/{iin[0]}/{iin[:4]}.yml")


def load_iin(iin):
    """Return a Python Object from the Loaded Yaml Data File."""
    path = build_iin_path(iin)
    with open(path, "r") as fl:
        document = load(fl, Loader=Loader)

    return document


if __name__ == "__main__":
    import sys

    if not len(sys.argv) > 1:
        testc = "554213561141250"
        testcc = "4542"
        print(json.dumps(load_iin(testcc)))
    else:
        testcc = sys.argv[1]
        if len(testcc) >= 6:
            print(json.dumps(load_iin(testcc).get(testcc[:6])))
        else:
            print(json.dumps(load_iin(testcc)))
