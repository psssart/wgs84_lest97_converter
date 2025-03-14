# setup.py

from setuptools import setup, find_packages

setup(
    name='wgs84_lest97_converter',
    version='0.1.0',
    description='Coordinate converter between WGS84 and L-Est97 using pyproj',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Pavel Shubin',
    author_email='pasubi@taltech.ee',
    url='https://github.com/psssart/wgs84_lest97_converter',
    packages=find_packages(),
    install_requires=[
        'pyproj==3.7.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
