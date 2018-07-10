import setuptools


setuptools.setup(
    name='eote-dice',
    version='1.0.0',

    description='Utility for analyzing EotE dice rolls.',
    long_description=open('README.rst').read(),
    keywords='star wars EotE dice role-playing',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/eote-dice',
    license='MIT',

    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,

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
