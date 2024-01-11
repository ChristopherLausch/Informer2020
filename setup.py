#!/usr/bin/env python
import io
import os
import re
import shutil
import sys

from pkg_resources import DistributionNotFound, get_distribution
from setuptools import find_packages, setup

#to import this package: clone it, then go to the package you want to install it to: pip install -e ../Informer2020/
#
#
# def read(*names, **kwargs):
#     with io.open(
#         os.path.join(os.path.dirname(__file__), *names),
#         encoding=kwargs.get("encoding", "utf8"),
#     ) as fp:
#         return fp.read()
#
#
# def get_dist(pkgname):
#     try:
#         return get_distribution(pkgname)
#     except DistributionNotFound:
#         return None
#
#
# def find_version(*file_paths):
#     version_file = read(*file_paths)
#     version_match = re.search(
#         r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
#     )
#     if version_match:
#         return version_match.group(1)
#     raise RuntimeError("Unable to find version string.")
#
#
# PATH_ROOT = os.path.dirname(__file__)
#
#
#
# def load_requirements(path_dir=PATH_ROOT, comment_char="#"):
#     with open(os.path.join(path_dir, "requirements.txt"), "r") as file:
#         lines = [ln.strip() for ln in file.readlines()]
#     reqs = []
#     for ln in lines:
#         # filer all comments
#         if comment_char in ln:
#             ln = ln[: ln.index(comment_char)]
#         if ln:  # if requirement is not empty
#             reqs.append(ln)
#     return reqs


setup(
    # Metadata
    name="informer_Test"
)