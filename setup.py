import os
from glob import glob
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

#  rm -R build/ dist/ *egg-info
#  python3 setup.py sdist
#  twine upload dist/*

SRC_FOLDER = 'src'
PKG_NAME = 'unicms_unical_storage_handler'

setup(
    name=PKG_NAME,
    version='0.8.3',

    packages=[PKG_NAME],
    package_dir={PKG_NAME: f"{SRC_FOLDER}/{PKG_NAME}"},

    package_data={PKG_NAME: [i.replace(f'{SRC_FOLDER}/{PKG_NAME}/', '')
                                   for i in glob(f'{SRC_FOLDER}/{PKG_NAME}/**',
                                                 recursive=True)]
    },

    license='Apache License 2.0',
    description="uniCMS handler to display data from storage.unical.it APIs",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/UniversitaDellaCalabria/unicms-unical-storage-handler',
    author='Giuseppe De Marco, Francesco Filicetti',
    author_email='giuseppe.demarco@unical.it, francesco.filicetti@unical.it',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'unicms-template-unical',
        'django-form-builder'
    ],
)
