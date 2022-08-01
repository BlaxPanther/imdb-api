from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='imdb-api',
    version='1.0',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)