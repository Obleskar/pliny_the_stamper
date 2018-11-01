from setuptools import setup, find_packages


with open('README.md', 'r') as infile:
    long_description = infile.read()

setup(
    name='pliny_the_stamper',
    version='0.1.0',
    description='Merge and bates number PDFs on the command line.',
    long_description=long_description,
    long_description_content_type='test/markdown',
    url='https://github.com/Obleskar/pliny_the_stamper.git',
    install_requires=['Click'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pliny = pliny:cli'
        ]
    }
)
