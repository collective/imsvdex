from setuptools import find_packages
from setuptools import setup


version = "1.2.dev0"

setup(
    name="imsvdex",
    version=version,
    description="Read/write vocabularies in IMS Vocabulary Definition Exchange format.",
    long_description=open("README.rst").read() + "\n" + open("CHANGES.txt").read(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="vocabulary xml vdex ims",
    author="Martin Raspe",
    author_email="raspe@biblhertz.it",
    url="https://github.com/collective/imsvdex",
    license="D-FSL - German Free Software License",
    packages=find_packages(),
    include_package_data=True,
    test_suite="imsvdex.tests",
    zip_safe=False,
    install_requires=["lxml",],
)
