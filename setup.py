import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'
DESCRIPTION = 'Download and install different web drivers'
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

setup(
    name="webdriver_installer",
    version=VERSION,
    author="riad-azz (Riadh Azzoun)",
    author_email="<riadh.azzoun@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["packaging", "requests"],
    keywords=['python', 'selenium', 'web', 'browser', 'webdriver installer', 'webdriver', "download webdriver"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
