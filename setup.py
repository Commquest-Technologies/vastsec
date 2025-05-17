from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vastsec/__init__.py
from vastsec import __version__ as version

setup(
	name="vastsec",
	version=version,
	description="Vast Security Custom Apps",
	author="Commquest Technologies (Pty) Ltd.",
	author_email="info@commquest.co.za",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
