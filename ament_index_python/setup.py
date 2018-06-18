from setuptools import find_packages
from setuptools import setup

setup(
    name='ament_index_python',
    version='0.5.1',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Dirk Thomas',
    maintainer_email='dthomas@osrfoundation.org',
    url='https://github.com/ament/ament_index',
    download_url='https://github.com/ament/ament_index/releases',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Python API to access the ament resource index.',
    long_description="""\
A Python API to find resources based on their type in the ament resource index
and get the content of individual resources.""",
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
)
