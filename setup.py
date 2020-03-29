import setuptools


setuptools.setup(
    name='eote-dice',
    version='1.2.0',

    description='Utility for analyzing Star Wars Edge of the Empire (EotE) dice rolls.',
    long_description=open('README.rst').read(),
    keywords='star wars EotE dice role-playing',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/eote-dice',

    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3.5',
    zip_safe=False,

    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],

    py_modules=['eote_dice', 'dice', 'distribution'],

    scripts=['eote_dice.py'],

    entry_points={
        'console_scripts': [
            'eote_dice = eote_dice:main',
        ],
    }
)
