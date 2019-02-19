from __future__ import division, absolute_import, print_function

from os.path import join, sep, dirname

import pytest

from numpy.distutils.misc_util import (
    appendpath, minrelpath, gpaths, get_shared_lib_extension, get_info, Configuration
    )
from numpy.testing import (
    assert_, assert_equal, assert_raises
    )

ajoin = lambda *paths: join(*((sep,)+paths))

class TestAppendpath(object):

    def test_1(self):
        assert_equal(appendpath('prefix', 'name'), join('prefix', 'name'))
        assert_equal(appendpath('/prefix', 'name'), ajoin('prefix', 'name'))
        assert_equal(appendpath('/prefix', '/name'), ajoin('prefix', 'name'))
        assert_equal(appendpath('prefix', '/name'), join('prefix', 'name'))

    def test_2(self):
        assert_equal(appendpath('prefix/sub', 'name'),
                     join('prefix', 'sub', 'name'))
        assert_equal(appendpath('prefix/sub', 'sup/name'),
                     join('prefix', 'sub', 'sup', 'name'))
        assert_equal(appendpath('/prefix/sub', '/prefix/name'),
                     ajoin('prefix', 'sub', 'name'))

    def test_3(self):
        assert_equal(appendpath('/prefix/sub', '/prefix/sup/name'),
                     ajoin('prefix', 'sub', 'sup', 'name'))
        assert_equal(appendpath('/prefix/sub/sub2', '/prefix/sup/sup2/name'),
                     ajoin('prefix', 'sub', 'sub2', 'sup', 'sup2', 'name'))
        assert_equal(appendpath('/prefix/sub/sub2', '/prefix/sub/sup/name'),
                     ajoin('prefix', 'sub', 'sub2', 'sup', 'name'))

class TestMinrelpath(object):

    def test_1(self):
        n = lambda path: path.replace('/', sep)
        assert_equal(minrelpath(n('aa/bb')), n('aa/bb'))
        assert_equal(minrelpath('..'), '..')
        assert_equal(minrelpath(n('aa/..')), '')
        assert_equal(minrelpath(n('aa/../bb')), 'bb')
        assert_equal(minrelpath(n('aa/bb/..')), 'aa')
        assert_equal(minrelpath(n('aa/bb/../..')), '')
        assert_equal(minrelpath(n('aa/bb/../cc/../dd')), n('aa/dd'))
        assert_equal(minrelpath(n('.././..')), n('../..'))
        assert_equal(minrelpath(n('aa/bb/.././../dd')), n('dd'))

class TestGpaths(object):

    def test_gpaths(self):
        local_path = minrelpath(join(dirname(__file__), '..'))
        ls = gpaths('command/*.py', local_path)
        assert_(join(local_path, 'command', 'build_src.py') in ls, repr(ls))
        f = gpaths('system_info.py', local_path)
        assert_(join(local_path, 'system_info.py') == f[0], repr(f))

class TestSharedExtension(object):

    def test_get_shared_lib_extension(self):
        import sys
        ext = get_shared_lib_extension(is_python_ext=False)
        if sys.platform.startswith('linux'):
            assert_equal(ext, '.so')
        elif sys.platform.startswith('gnukfreebsd'):
            assert_equal(ext, '.so')
        elif sys.platform.startswith('darwin'):
            assert_equal(ext, '.dylib')
        elif sys.platform.startswith('win'):
            assert_equal(ext, '.dll')
        # just check for no crash
        assert_(get_shared_lib_extension(is_python_ext=True))


class TestAddData(object):

    def test_data_dir_raises(self):
        """
        Test that invalid input to the method raises the correct TypeError.
        """

        config = Configuration()
        with pytest.raises(TypeError) as exepinfo:
            config.add_data_dir(0)

        assert_(str(exepinfo.value) == 'not a string: 0')

    def test_data_files_raises(self):
        """
        Test that invalid input to the method raises the correct TypeError.
        """

        config = Configuration()
        with pytest.raises(TypeError) as exepinfo:
            config.add_data_files(0)
        expected_return = 'expected str, bytes or os.PathLike object, not int'

        assert_(str(exepinfo.value) == expected_return)

def test_installed_npymath_ini():
    """
    Regression test for gh-7707.  If npymath.ini wasn't installed, then this
    will give an error.
    """
    info = get_info('npymath')

    assert isinstance(info, dict)
    assert "define_macros" in info

def test_add_data_files_TypeError():
    # ensures that if called a none value, add_data_files raises exception
    c = Configuration()
    with assert_raises(TypeError):
         c.add_data_files(None)

def test_add_data_dir():
    """
    Mocks a config object with empty data_files
    ensures that no data is added and no exceptions are rasied
    """
    class mock(Configuration):
        def get_distribution(self):
            return mockDist()
    class mockDist():
        datafiles = "something"
        data_files = []

    c = mock()
    c.add_data_dir('fun')
    assert_equal([], c.data_files)

def test_add_data_files():
    """
    Mocking a config object with get_dist returns None
    ensures that no errors are raised and empty file is added
    """
    class mock(Configuration):
        def get_distribution(self):
            return None

    c = mock()
    c.add_data_files('fun')
    assert_equal([('', [])], c.data_files)
