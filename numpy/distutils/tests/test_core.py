from __future__ import division, print_function

import pytest
from numpy.distutils.core import setup as core_setup

class _lib_class:
    libraries = 1

def test_setup_type_error():
    lib = _lib_class

    attr = { 'ext_modules': [lib] }
    with pytest.raises(TypeError):
        core_setup(**attr)
