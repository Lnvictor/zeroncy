# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='zeroncy',
      version='0.1',
      description='Zero dependency lib for python',
      long_description=open(README).read(),
      long_description_content_type='text/markdown',
      author="Victor Pereira", author_email="vh141299@gmail.com",
      license="GNU 3.0",
      py_modules=['zeroncy'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/Lnvictor/zeroncy/',)
