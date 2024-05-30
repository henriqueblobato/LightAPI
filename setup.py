import codecs

from setuptools import setup, find_packages

with codecs.open('README.md', 'r', 'utf-8') as file:
    long_description = file.read()

setup(
    name='LightApi',
    version='0.1.0',
    description='A lightweight framework for building API endpoints using Python\'s native libraries.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['api', 'rest', 'restful', 'endpoint', 'lightweight', 'framework'],
    author='iklobato',
    author_email='iklobato1@gmail.com',
    url='https://github.com/henriqueblobato/LightApi',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy==2.0.30',
        'aiohttp==3.9.5',
    ],
    extras_require={
        'test': ['pytest'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_data={
        '': ['alembic.ini', 'migrations/script.py.mako'],
    },
    entry_points={
        'console_scripts': [
            'lightapi = cli:main',
        ],
    },
    python_requires='>=3.11',
)
