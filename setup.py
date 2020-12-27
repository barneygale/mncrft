from distutils.core import setup

setup(
    name='mncrft',
    version='1.0',
    author='Barney Gale',
    author_email='barney@barneygale.co.uk',
    url='https://github.com/barneygale/mncrft',
    license='MIT',
    description='Minecraft data types library',
    long_description=open('README.rst').read(),
    install_requires=['bitstring >= 3.1.0'],
    test_requires=['pytest'],
    packages=[
        "mncrft",
        "mncrft.buffer",
        "mncrft.data_pack",
        "mncrft.packet",
    ],
    package_data={'mncrft': [
        'packet/data/*.csv',
        'data_pack/data/*.nbt']},
)
