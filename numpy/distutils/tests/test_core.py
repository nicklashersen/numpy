from __future__ import division, print_function

import pytest
from unittest import mock

from numpy.distutils.core import setup as core_setup

class _lib_class:
    libraries = 1

class _setup_return_class:
    help = True
    

def test_setup_type_error():
    lib = _lib_class

    attr = { 'ext_modules': [lib] }
    with pytest.raises(TypeError):
        core_setup(**attr)

@mock.patch("numpy.distutils.core.old_setup", return_value=_setup_return_class, autospec=True)
def test_setup_dist_help(mock_old_setup):
    attr = { 'configuration': [] }

    core_setup(**attr)
