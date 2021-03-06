from __future__ import division, print_function

import pytest
from unittest import mock

from numpy.distutils.core import setup as core_setup

class _lib_class:
    libraries = [ None ]

class _setup_return_class:
    help = True
    
class _ext_string_lib:
    libraries = "somelib"

def test_setup_type_error():
    """
    Test that setup ext_modules throws an Type error
    if the ext module list isn't a sequence or string.
    """
    lib = _lib_class

    attr = { 'ext_modules': [lib] }
    with pytest.raises(TypeError):
        core_setup(**attr)

@mock.patch("numpy.distutils.core.old_setup", return_value=_setup_return_class, autospec=True)
def test_setup_dist_help(mock_old_setup):
    """
    Test the configuration help branch in setup. 
    """
    attr = { 'configuration': [] }

    assert core_setup(**attr).help == True

@mock.patch("numpy.distutils.core.old_setup", return_value=_setup_return_class, autospec=True)
def test_setup_ext_library_string(mock_setup):
    """
    Test the ext_modules branch in setup for strings returns
    the correct result.
    """
    lib = _ext_string_lib
    attr = { 'ext_modules': [lib] }
    core_setup(**attr)

    assert attr['ext_modules'][0].libraries == list('somelib') 
