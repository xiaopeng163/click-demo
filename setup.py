from setuptools import setup

setup(
    name='clickctl',
    version='1.0',
    packages=['clickctl', 'clickctl.commands'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        clickctl=clickctl.cli:cli
    ''',
)
