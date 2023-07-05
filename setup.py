from __future__ import absolute_import
from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='imdb-page-api',
    version='1.0.3',
    description='A useful API to scrap movie/series/video details available on IMDb.',
    license='GNU General Public License v3.0',
    author="BlaxPanther",
    packages=["imdb_api"],
    url='https://github.com/BlaxPanther/imdb-api.git',
    keywords='python, imdb, movie-api, imdb-webscrapping, imdb-api, imdb-python, imdb-scraper',
    install_requires=["requests==2.26.0","beautifulsoup4==4.10.0","html5lib>=0.999999999", "selenium>0.9999999999"],
    zip_safe=False,
    classifiers=[
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    ]

)

