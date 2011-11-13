"""A Python script to build the _tifffile extension module.

Usage:: ``python setup.py build_ext --inplace``

"""

from distutils.core import setup, Extension
import numpy

setup(name='_tifffile',
    ext_modules=[
      Extension(
        '_tifffile', ['tifffile.c'],
        include_dirs=[numpy.get_include()],
        extra_compile_args=[])],
  py_modules=["tifffile"],
)
