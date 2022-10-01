from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '0.0.1'
DESCRIPTION = 'Download and install different web drivers'
LONG_DESCRIPTION = 'A package that will help you to download and save the latest versions of web drivers.'


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
        "Development Status :: 1 - Released",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)