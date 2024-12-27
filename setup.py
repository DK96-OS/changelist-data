"""Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="changelist-data",
    version="0.1.5",
	description='Data package for Changelists CLI Tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
	author='DK96-OS',
	url='https://github.com/DK96-OS/changelist-data/',
	project_urls={
        "Issues": "https://github.com/DK96-OS/changelist-data/issues",
        "Source Code": "https://github.com/DK96-OS/changelist-data/"
	},
	license='GPLv3',
    packages=find_packages(exclude=['test', 'test.*']),
    entry_points={
        'console_scripts': [],
    },
    python_requires='>=3.10',
    keywords=['changelist', 'vcs'],
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
