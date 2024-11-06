"""Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="changelist-data",
    version="0.1",
	author='DK96-OS',
	description='Data Management base package for Changelists CLI Tools',
	url='https://github.com/DK96-OS/changelist-data/',
	project_urls={
        "Issues": "https://github.com/DK96-OS/changelist-data/issues",
        "Source Code": "https://github.com/DK96-OS/changelist-data/"
	},
	license='GPLv3',
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [],
    },
    python_requires='>=3.10',
    keywords=['changelist', 'vcs']
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
