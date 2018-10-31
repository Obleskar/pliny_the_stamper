from setuptools import setup


setup(name='pliny_the_stamper',
      version='0.1.0',
      py_modules=['main.py'],
      install_requires=['Click'],
      entry_points='''[console_scripts] pliny=pliny:cli''')
