from setuptools import setup

setup(
    name='openexchangerates',
    version='1.0.0',
    description='openexchangerates.org python API client (forked in version 3)',
    long_description=open('README.rst').read(),
    url='https://github.com/asosnovsky/openexchangerates',
    license='MIT',
    author='Individual',
    author_email='ariel@sosnovsky.ca',
    packages=['openexchangerates'],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'httpretty',
        'mock'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
