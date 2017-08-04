"""A setuptools based setup module for Mawdoo3's Ask API"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='flask_webservice_skeleton',
    version='dev01',
    description="Sample Flask API",
    url='https://github.com/mjalajel/flask-minimal-webservice',
    author='Mahmoud Jalajel',
    author_email='m@jalajel.net',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    keywords='flask api microservice',
    packages=find_packages(),
    py_modules=['app'],
    install_requires=[
        'click',
        'flask',
    ],
    test_suite='nose2.collector.collector',
    extras_require={
        'test': ['nose2', 'cov-core'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'flask-api=app:run',
        ],
    },
)
