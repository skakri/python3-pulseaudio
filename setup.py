#!/usr/bin/env python

from distutils.core import setup

setup(name='libpulseaudio3',
      version='1.0',
      description='simple libpulseaudio bindings for python 3',
      author='Kristaps Karlsons',
      author_email='kristaps.karlsons@gmail.com',
      license='LGPL',
      url='http://github.com/skakri/python3-pulseaudio',
      packages=['pulseaudio'],
      provides=['libpulseaudio3']
     )
